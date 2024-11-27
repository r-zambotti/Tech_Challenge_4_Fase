########### Importação das bibliotecas ########### 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split


########### Configuração do layout ########### 
st.set_page_config(
    page_title="Portal de Preços do Petróleo",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

navegacao = ['Portal', 'Dashboard', 'Previsões']
pagina = st.sidebar.selectbox('Navegação', navegacao)

########### Carregar dados ########### 
df_streamlit = pd.read_csv('df_streamlit.csv')

########### Configuração da página inicial ########### 
if pagina == 'Portal':
    st.header('Portal de Preços do Petróleo', divider='blue')
    st.subheader('Definição')
    st.write('O Portal de Preços do Petróleo é o aplicativo de gerenciamento do preço bruto do barril de petróleo brent')
    st.subheader('Dados')
    st.write('Os dados foram obtidos no site do Instituto de Pesquisa Econômica Aplicada (Ipea) e podem ser acessados por meio do link:')
    st.write('Clique [aqui](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view) para acessar os dados do Ipea')
    st.subheader('O que é o Ipea ?')
    st.write('O Instituto de Pesquisa Econômica Aplicada (Ipea) é uma fundação pública federal vinculada ao Ministério do Planejamento e Orçamento.')
    st.subheader('O que é o Petróleo Brent ?')
    st.write('Produzido no Mar do Norte (Europa), Brent é uma classe de petróleo bruto que serve como benchmark para o preço internacional de diferentes tipos de petróleo.') 
    st.write('Neste caso, é valorado no chamado preço FOB (free on board), que não inclui despesa de frete e seguro no preço.')
    st.subheader('Autor')
    st.write('Jorge Luiz Chumbo') 

########### Configuração do dashboard ###########     
if pagina == 'Dashboard':
    st.header('Evolução Preço Bruto do Petróleo Brent (FOB)', divider='blue')

    # Barra lateral
    with st.sidebar:  
        lista_ano = list(df_streamlit.ano.unique())[::]
        ano_selecionado = st.selectbox('Selecione o Ano', lista_ano, index=len(lista_ano)-1)
        df_ano_selecionado = df_streamlit[df_streamlit.ano == ano_selecionado]
        df_ano_selecionado_sorted = df_ano_selecionado.sort_values(by='data', ascending=True)

    # Funções
    def calcula_ultimo_valor_atual(df):
        valor_atual = df.preco.iloc[-1]
        data_atual = df.data.iloc[-1]
        delta_atual = df['variacao_%'].iloc[-1]
        return valor_atual, data_atual, delta_atual
    
    def calcula_maior_menor_valor(df):
        maior_valor = df.preco.max()
        maior_valor_data = df[df.preco == maior_valor]['data'].max()
        menor_valor = df.preco.min()
        menor_valor_data = df[df.preco == menor_valor]['data'].max()
        return maior_valor, maior_valor_data, menor_valor, menor_valor_data
    
    def calcula_valor_medio(df):
        valor_medio = df.preco.mean().round(2)
        return valor_medio

    # Colunas
    col = st.columns((2.5, 8), gap='medium')

    with col[0]:
        st.markdown('#### Último Fechamento')

        if ano_selecionado >= 2019:
            valor = calcula_ultimo_valor_atual(df_ano_selecionado_sorted)[0]
            data = calcula_ultimo_valor_atual(df_ano_selecionado_sorted)[1]
            delta = calcula_ultimo_valor_atual(df_ano_selecionado_sorted)[2]

        st.metric(label=data, value=f'{valor} US$', delta=f'{delta} %')

        st.markdown('#### Maior Valor Fechado')

        if ano_selecionado >= 2019:
            valor = calcula_maior_menor_valor(df_ano_selecionado_sorted)[0]
            data = calcula_maior_menor_valor(df_ano_selecionado_sorted)[1]

        st.metric(label=data, value=f'{valor} US$')

        st.markdown('#### Menor Valor Fechado')

        if ano_selecionado >= 2019:
            valor = calcula_maior_menor_valor(df_ano_selecionado_sorted)[2]
            data = calcula_maior_menor_valor(df_ano_selecionado_sorted)[3]

        st.metric(label=data, value=f'{valor} US$')

        st.markdown('#### Valor Médio Anual')

        if ano_selecionado >= 2019:
            valor = calcula_valor_medio(df_ano_selecionado_sorted)
            ano = str(ano_selecionado)

        st.metric(label=ano, value=f'{valor} US$')

    with col[1]:
        st.markdown('#### Preço Histórico (US$)')

        if ano_selecionado >= 2019:
            df_ano_selecionado_sorted_grafico = df_ano_selecionado_sorted.rename(columns={'data': 'Data', 'preco':'Preço (US$)'})
            st.line_chart(data=df_ano_selecionado_sorted_grafico, x='Data', y='Preço (US$)', color=None, width=0, height=0, use_container_width=True)

        st.markdown('#### Variação Percentual (%)')

        if ano_selecionado >= 2019:
            df_ano_selecionado_sorted_grafico = df_ano_selecionado_sorted.rename(columns={'data': 'Data', 'variacao_%':'Variação (%)'})
            st.line_chart(data=df_ano_selecionado_sorted_grafico, x='Data', y='Variação (%)', color=None, width=0, height=0, use_container_width=True)


########### Configuração da página de previsões ###########
if pagina == 'Previsões':
    st.header('Previsões', divider='blue')

    # Funções
    def aplica_modelo(df, lags:int):
        base_modelo = df.copy()
        base_modelo = df[['data', 'preco']]
        base_modelo = base_modelo.sort_values(by='data', ascending=True).reset_index(drop=True)
        for lag in range(1, lags + 1):
            base_modelo[f'preco_lag_{lag}'] = base_modelo['preco'].shift(lag)
        base_modelo = base_modelo.dropna()
        X = base_modelo[['preco_lag_1']].values
        y = base_modelo[['preco']].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False, random_state=42)
        reg_gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42, loss='squared_error')
        reg_gb.fit(X_train, y_train)
        previsoes = reg_gb.predict(X_test)
        MSE = mean_squared_error(y_test, previsoes)
        MAE = mean_absolute_error(y_test, previsoes)
        #ultimo_valor = X[-1].reshape(1, -1)
        valores_previstos= []
        for lag in range(lags):
            ultimo_valor = X[-lag].reshape(1, -1)
            proximo_valor = reg_gb.predict(ultimo_valor)[0]
            valores_previstos.append(proximo_valor)
            ultimo_valor = np.roll(ultimo_valor, -1)
            ultimo_valor[0, -1] = proximo_valor
        datas_previstas = pd.date_range(base_modelo['data'].iloc[-1], periods=lags + 1)[1:]
        datas_atuais = base_modelo['data'].iloc[-lags:]
        valores_atuais = base_modelo['preco'].iloc[-lags:]
        base_prevista = pd.DataFrame(zip(datas_previstas, valores_previstos), columns=['datas_previstas', 'valores_previstos'])
        base_prevista['datas_previstas'] = base_prevista['datas_previstas'].apply(lambda x: x.strftime('%Y-%m-%d'))
        return base_modelo, base_prevista, MSE, MAE
    
    

    # Colunas
    col = st.columns((3, 7), gap='medium')

    with col[0]:
        st.markdown('#### Datas e Valores Previstos')

        # Número de dias selecionados para previsão
        numero_lags = st.slider("Selecione quantos dias de previsão deseja obter:", 5, 30, 5)

        df_previsao = aplica_modelo(df_streamlit, numero_lags)[1]
        df_previsao_grafico = df_previsao.rename(columns={'datas_previstas': 'Data Prevista', 'valores_previstos':'Preço Previsto (US$)'})

        erro_mse = aplica_modelo(df_streamlit, numero_lags)[2]
        erro_mae = aplica_modelo(df_streamlit, numero_lags)[3]

        st.table(df_previsao_grafico)

    with col[1]:

        st.markdown('#### Evolução dos Valores Previstos')
        st.line_chart(data=df_previsao_grafico, x='Data Prevista', y='Preço Previsto (US$)', color='#FFA500', width=0, height=0, use_container_width=True)