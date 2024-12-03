import requests
import pandas as pd
from bs4 import BeautifulSoup

from prophet import Prophet
from prophet.serialize import model_to_json, model_from_json

def acrescentar_um_dia(data):
    data = data + pd.Timedelta(days=1)
    return data

def extrair_dados_ipeadata(url):
    """
    Extrai os dados da tabela da página do ipeadata e retorna um DataFrame do pandas.

    Parâmetros:
    url (str): URL da página do ipeadata.

    Retorna:
    DataFrame: Dados extraídos da tabela.
    """
    # Fazendo a requisição HTTP para a página
    response = requests.get(url)

    # Verificando o status da requisição
    if response.status_code == 200:
        print("Conexão bem-sucedida!")
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None

    # Parseando o HTML com BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Buscando a tabela na página
    table = soup.find("table", {"class": "dxgvTable"})  # Identifique a classe correta da tabela
    if table:
        # Extraindo os dados da tabela
        rows = table.find_all("tr")
        data = []

        # Iterando pelas linhas da tabela
        for row in rows:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            if cols:  # Ignorar linhas vazias
                data.append(cols)

        # Convertendo os dados para um DataFrame do pandas
        columns = ["Data", "Preço", "drop1", "drop2", "drop3", "drop4"]  # Ajuste conforme as colunas da tabela
        df_dados = pd.DataFrame(data, columns=columns)

        # Deletando as colunas desnecessárias
        df_dados = df_dados.drop(columns=["drop1", "drop2", "drop3", "drop4"])

        # Deletando as 3 primeiras linhas
        df_dados = df_dados.iloc[3:]

        return df_dados
    else:
        print("Tabela não encontrada na página.")
        return None

def processar_dados(df_dados):
    # Renomeando as colunas
    df_ipea = df_dados.rename(columns={"Data": "data", "Preço": "preco"})

    # Convertendo a coluna 'data' para o tipo datetime
    df_ipea["data"] = pd.to_datetime(df_ipea["data"], format="%d/%m/%Y")

    # Convertendo a coluna 'preco' para float
    df_ipea['preco'] = df_ipea['preco'].str.replace(',', '.').astype(float)

    # Setando data como INDEX
    df_ipea = df_ipea.set_index('data')

    # Preenchendo os dias faltantes (FDS + Feriados)
    df_ipea = df_ipea.asfreq('D').ffill()

    # reset do index
    df_ipea = df_ipea.reset_index()

    # Criando a coluna 'abertura' baseada no preço do dia anterior
    df_ipea['open'] = df_ipea['preco'].shift(1)
    df_ipea['open'] = df_ipea['open'].fillna(df_ipea['preco'])  # Preencher o primeiro valor com o preço original

   # Renomeando as colunas para uso no prophet
    df_ipea = df_ipea.rename(columns={"data": "ds", "preco": "y"})

    return df_ipea

def filtrar_dados_prophet(df, anos_historico=1):
    """
    Filtra os dados do df para uso no treinamento do prophets.

    Parâmetros:
    df (DataFrame): Dados a serem filtrados.
    anos_historico (int): Anos de historico.

    Retorna:
    DataFrame: Dados filtrados da tabela.
    """
    # Encontrar a data máxima 
    data_maxima = df['ds'].max() 
    # Calcular a data limite (um ano antes da data máxima) 
    data_limite = data_maxima - pd.DateOffset(years=anos_historico) 
    # Filtrar os dados para incluir apenas os últimos 12 meses 
    df_filtrado = df[df['ds'] >= data_limite]
    return df_filtrado

def dividir_treino_teste(df, dias_teste=5):
    # Tamanho do conjunto de treino 
    train_size = df.shape[0] - dias_teste 
    
    # Dividindo os dados em treino e teste 
    train = df[:train_size] 
    test = df[train_size:] 
    
    return train, test


def modelar_prophet(train, test):
    """
    Treina e testa um modelo Prophet com os dados fornecidos.

    Parâmetros:
    train (DataFrame): Dados de treino.
    test (DataFrame): Dados de teste.

    Retorna:
    tuple: DataFrame das previsões, métricas de desempenho do modelo.
    """
    # Renomear colunas para compatibilidade com Prophet
    train_prophet = train
    test_prophet = test

    # Criar e treinar o modelo Prophet
    model = Prophet(daily_seasonality=True)
    model.add_regressor("open")
    model.fit(train_prophet)

    # Criar DataFrame para previsões futuras
    future = model.make_future_dataframe(periods=len(test), include_history=True)
    future["open"] = pd.concat([train["open"], test["open"]], ignore_index=True)
    
    # Fazer previsões
    forecast = model.predict(future)

    # Obter as previsões para o período de teste
    preds = forecast[["ds", "yhat"]].tail(len(test))
    preds = preds.set_index("ds")
    y_test = test_prophet.set_index("ds")["y"]

    # Salvando o modelo em JSON
    with open('modelo_prophet.json', 'w') as f: f.write(model_to_json(model))

    return preds, forecast

def adicionar_registro(df, novo_registro):
    """
    Adiciona um novo registro ao DataFrame.

    Parâmetros:
    df (DataFrame): DataFrame existente.
    novo_registro (dict): Novo registro a ser adicionado ao DataFrame.

    Retorna:
    DataFrame: DataFrame com o novo registro adicionado.
    """
    # Converter o dicionário do novo registro em um DataFrame
    df_novo_registro = pd.DataFrame([novo_registro])
    
    # Adicionar o novo registro ao DataFrame existente
    df = pd.concat([df, df_novo_registro], ignore_index=True)
    
    return df

def utilizar_prophet(train, test):
    """
    Treina e testa um modelo Prophet com os dados fornecidos.

    Parâmetros:
    train (DataFrame): Dados de treino.
    test (DataFrame): Dados de teste.

    Retorna:
    tuple: DataFrame das previsões, métricas de desempenho do modelo.
    """
    # Renomear colunas para compatibilidade com Prophet
    train_prophet = train
    test_prophet = test

    # Carregar o modelo salvo em JSON 
    with open('modelo_prophet.json', 'r') as f:
        model = model_from_json(f.read())

    # Criar DataFrame para previsões futuras
    future = model.make_future_dataframe(periods=len(test), include_history=True)
    future["open"] = pd.concat([train["open"], test["open"]], ignore_index=True)
    
    # Fazer previsões
    forecast = model.predict(future)

    # Obter as previsões para o período de teste
    preds = forecast[["ds", "yhat"]].tail(len(test)-10) # -10 devido a quantidade separada para gerar o modelo
    preds = preds.set_index("ds")
    preds = preds.reset_index()
    y_test = test_prophet.set_index("ds")["y"]

    # Salvando o modelo em JSON
    with open('modelo_prophet.json', 'w') as f: f.write(model_to_json(model))

    return preds, forecast