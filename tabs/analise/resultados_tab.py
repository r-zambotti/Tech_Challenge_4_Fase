import streamlit as st
from tabs.tab import TabInterface


class ResultadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":gray[Examinando a Fonte dos Dados]", divider="orange")

            st.markdown(
                """
                Os dados históricos do preço do petróleo foram extraídos do site do Instituto de Pesquisa Econômica Aplicada (Ipea). O Ipea disponibiliza uma série temporal detalhada com valores diários do preço do petróleo. Na data da exportação, foram obtidos os preços que abrangem o período de 20 de maio de 1987 até 20 de maio de 2024.\n
                Esses dados foram salvos em um arquivo Microsoft Excel, preparando-os para uma análise subsequente em Python. Esta preparação permite utilizar ferramentas avançadas de análise e visualização para explorar a variação dos preços ao longo do tempo.
                """
            )
            st.subheader(":orange[Análise Visual da Variação ao Longo do Tempo]")
            st.markdown(
                """
                Para visualizar a variação do preço do petróleo ao longo do tempo, criamos um gráfico utilizando Python. Nele, as datas estão plotadas no eixo **X** e os preços do petróleo no eixo **Y**. Essa visualização clara e intuitiva permite observar como os preços do petróleo oscilaram entre 20 de maio de 1987 e 20 de maio de 2024. O gráfico facilita a identificação de tendências, padrões e flutuações significativas, proporcionando uma visão abrangente e precisa das mudanças ao longo do tempo.\n
                Primeiramente foi instalado as bibliotecas e realizada as importações.
                """
            )
            st.image('assets/img/Python_Fig_1.png', caption='Instalação de Bibliotecas e Importação de Módulos')

            st.markdown(
                """
                Em seguida, foi feito o upload do arquivo Excel no Google Colab.
                """
            )  

            st.image('assets/img/Python_Fig_2.png', caption='Upload do Arquivo Excel no Google Colab', use_column_width=True, output_format='auto')

            st.markdown(
                """
                Para ler o arquivo Excel contendo os dados históricos do preço do petróleo, utilizamos a função **:gray[`read_excel()`]** da biblioteca **Pandas** em Python. No arquivo, a coluna originalmente nomeada como "**Brent**" foi renomeada para "**Close**" para fins estéticos e de padronização, sem afetar os resultados da análise.
                """
            ) 
            st.markdown(
                """
                Após a leitura dos dados, executamos o método **:gray[`.info()`]** no DataFrame resultante. Este método fornece uma visão geral da estrutura do DataFrame, incluindo informações sobre o número de entradas, os tipos de dados em cada coluna e a quantidade de valores nulos. Essa inspeção preliminar é fundamental para entender a composição dos dados e preparar as etapas subsequentes de análise.
                """
            )

            st.image('assets/img/Python_Fig_3.png', caption='Leitura e Renomeação de Colunas no DataFrame', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                Com o DataFrame contendo os dados do preço do petróleo em mãos, podemos criar o gráfico utilizando o código abaixo.
                """
            )

            st.image('assets/img/Python_Fig_4.png', caption='Código para Criação de Gráfico de Linha com Matplotlib', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                O gráfico resultante pode ser visualizado abaixo. Ele representa todas as variações do preço do petróleo ao longo dos anos, mostrando as altas e baixas do mercado.\n
                Este gráfico oferece uma representação visual clara e intuitiva da flutuação dos preços do petróleo ao longo do tempo, permitindo a identificação de tendências de mercado e padrões de comportamento significativos.
                """
            )

            st.image('assets/img/Python_Fig_5.png', caption='Gráfico de Variação Histórica do Preço do Petróleo (1987-2024)', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                Para a análise utilizando o modelo LSTM, foi decidido que não era necessário considerar todos os dados desde 1987. Portanto, uma data de corte foi estabelecida para limitar o conjunto de dados. A data escolhida foi o dia 03 de maio de 2020. Isso significa que trabalharemos com quatro anos de dados históricos do preço do petróleo, a partir dessa data.\n
                Essa escolha foi baseada não apenas em considerações temporais, mas também na análise do desempenho das métricas, incluindo o **Coeficiente de Determinação (R²)**, o **Erro Médio Quadrático (MSE)**, o **Erro Médio Absoluto (MAE)**, o **Erro Percentual Absoluto Médio (MAPE)** e a **Raiz do Erro Médio Quadrático (RMSE)**. É importante encontrar um equilíbrio, pois muitos dados podem levar ao overfitting, enquanto uma base de dados limitada pode resultar em um desempenho pobre do modelo.\n
                Com base nessas análises, foi determinado que o período de quatro anos forneceria dados suficientes para treinar um modelo robusto de previsão de preços do petróleo, sem comprometer sua capacidade de generalização.\n
                Dito isso, foi aplicado o filtro no dataframe original e o gráfico foi gerado novamente.\n
                Abaixo o código Python desenvolvido.
                """
            )

            st.image('assets/img/Python_Fig_6.png', caption='Código para Criação de Gráfico do Preço do Petróleo a partir de 03/05/2020', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                Gráfico obtido após filtro com a data de corte.
                """
            )

            st.image('assets/img/Python_Fig_7.png', caption='Gráfico de Variação do Preço do Petróleo (2020-2024) com Dados Filtrados', use_column_width=True, output_format='auto')
 
            st.subheader(":orange[Construção do modelo LSTM]")

            st.markdown(
                """
                Com a análise preliminar dos dados concluída, avançamos para a construção do modelo LSTM. Desenvolvemos o código abaixo para alcançar os resultados que serão apresentados posteriormente neste trabalho.\n
                O código a seguir, realiza etapas importantes no processamento e preparação dos dados históricos do preço do petróleo para análise.\n 
                :one: **Leitura do arquivo Excel:** O primeiro passo é ler os dados históricos do preço do petróleo de um arquivo Excel chamado 'Petroleo.xlsx' e armazená-los em um DataFrame pandas chamado 'df'.\n
                :two: **Renomeação da coluna 'Brent' para 'Close':** A coluna que contém os preços do petróleo é renomeada de 'Brent' para 'Close' por motivos de padronização e conveniência.\n
                :three: **Filtragem dos dados após a data de corte:** Os dados são filtrados para incluir apenas as observações após a data de corte especificada. Isso significa que estamos interessados apenas nos dados mais recentes para nossa análise.\n
                :four: **Criação e manipulação do DataFrame 'data':** Os dados filtrados são copiados para o DataFrame 'data', que será usado para a manipulação e análise subsequentes. É importante notar que 'data' é uma cópia dos dados filtrados, portanto, quaisquer alterações feitas em 'data' não afetarão o DataFrame original 'df'.\n
                :five: **Reset Index:** Realiza a redefinição dos índices do DataFrame data, de forma que o índice original seja descartado e um novo índice numérico seja atribuído às linhas.\n
                :six: **Normalização dos dados:** Os preços do petróleo são normalizados usando a função **:gray[`MinMaxScaler()`]** do **scikit-learn**. A normalização é uma etapa importante no pré-processamento dos dados, pois coloca todas as características em uma escala comum, o que pode melhorar o desempenho do modelo.\n
                :seven: **Divisão dos dados em conjuntos de treinamento e teste:** Os dados normalizados são divididos em conjuntos de treinamento e teste. O conjunto de treinamento contém 80% dos dados, enquanto o conjunto de teste contém os 20% restantes. Essa divisão é importante para avaliar o desempenho do modelo em dados não vistos.

                """
            )

            st.image('assets/img/Python_Fig_8.png', caption='Etapas de Processamento e Preparação dos Dados para a Construção do Modelo LSTM', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                Continuando com a explicação do código, as próximas etapas são fundamentais para a construção e treinamento do modelo LSTM, visando prever os preços futuros do petróleo com base nos dados históricos processados. Vamos detalhar essas etapas a seguir:
                """
            )
            st.markdown(
                """
                :eight: **Definição da função 'create_sequences':** A função  recebe dois parâmetros: **dados**, que são os dados a serem preparados, e **sequence_length**, que define o tamanho das sequências de entrada e saída. A função itera sobre os dados e cria sequências de entrada e saída com base no comprimento especificado.\n 
                :nine: **Definição do comprimento da sequência:** O comprimento da sequência é definido como **:gray[`sequence_length = 10`]**. Isso significa que cada sequência de entrada conterá 10 pontos de dados, e o próximo ponto de dados será usado como saída correspondente.\n
                :one::zero: **Criação de sequências de entrada e saída para treinamento e teste:** A função **:gray[`create_sequences()`]** é chamada duas vezes, uma vez para os dados de treinamento (**train_data**) e outra vez para os dados de teste (**test_data**). Isso cria as sequências de entrada e saída necessárias para treinar e testar o modelo LSTM.\n
                :one::one: **Criação do modelo LSTM:** Um modelo LSTM é configurado utilizando a classe Sequential do *Keras*. Este modelo é composto por uma camada LSTM com 350 unidades, seguida por uma camada densa com uma única unidade de saída. A entrada do modelo é especificada como tendo a forma (**sequence_length**, **1**), onde **sequence_length** representa o comprimento das sequências e **1** indica que cada ponto de dado possui apenas uma característica.\n
                :one::two: **Compilação do modelo LSTM:** O modelo LSTM é compilado usando o otimizador *Adam* e a função de perda de erro quadrático médio (MSE).
                """
            )

            st.image('assets/img/Python_Fig_9.png', caption='Construção e treinamento do modelo LSTM para previsão de preços do petróleo', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                :one::three: **Treinamento do modelo LSTM:** O modelo LSTM é treinado usando os conjuntos de dados de treinamento **X_train** e **y_train**. A função **:gray[`fit()`]** é chamada com os parâmetros **:gray[`epochs=100`]** e **:gray[`batch_size=64`]**, indicando que o modelo será treinado por 100 épocas e que cada lote de dados terá 64 exemplos.\n
                :one::four: **Previsões com o modelo LSTM:** Após o treinamento, o modelo LSTM é usado para fazer previsões nos dados de teste (**X_test**). Isso é feito chamando a função **:gray[`predict()`]** no modelo, que retorna as previsões correspondentes para os dados de entrada.\n
                :one::five: **Cálculo das métricas de avaliação:** Diversas métricas de avaliação são calculadas para avaliar o desempenho do modelo LSTM em relação aos dados de teste. As métricas calculadas incluem:\n
                -  R² Score (Coeficiente de Determinação);
                -  MSE (Erro Quadrático Médio);
                -  MAE (Erro Médio Absoluto);
                -  MAPE (Erro Percentual Absoluto Médio);
                -  RMSE (Raiz do Erro Quadrático Médio).\n
                :one::six: **Impressão das métricas do modelo LSTM:** Por fim, as métricas calculadas são impressas na tela para que possam ser visualizadas e interpretadas. Isso fornece uma avaliação quantitativa do desempenho do modelo LSTM em relação aos dados de teste.
                """
            )

            st.image('assets/img/Python_Fig_10.png', caption='Treinamento e avaliação do modelo LSTM, incluindo previsões e métricas de desempenho', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                Com o uso deste código, obtivemos os seguintes resultados da análise de desempenho do modelo LSTM:\n
                - **R² Score (LSTM):** 0.8616
                - **MSE (LSTM):** 0.0003
                - **MAE (LSTM):** 0.0137
                - **MAPE (LSTM):** 2.4014%
                - **RMSE (LSTM):** 0.0173\n
                Seguindo com a análise do código, temos:\n
                **Função **:gray[`predict(num_prediction, model)`]**:** Esta função recebe dois parâmetros: **num_prediction**, que representa o número de pontos a serem previstos, e **model**, que é o modelo LSTM treinado. Ela inicialmente cria uma lista de previsões iniciando com os últimos **sequence_length** pontos da série temporal original (normalizada). Em seguida, itera **num_prediction** vezes, cada vez prevendo o próximo ponto da série temporal usando o modelo LSTM e adicionando-o à lista de previsões. Após todas as previsões serem feitas, a lista de previsões é desnormalizada usando o objeto *scaler* e retornada.\n
                **Função **:gray[`predict_dates(num_prediction)`]**:** Esta função gera as datas dos próximos **num_prediction** dias, com base na última data disponível na série temporal original. Ela utiliza a função **:gray[`pd.date_range()`]** do Pandas para criar uma sequência de datas a partir da última data disponível, e retorna uma lista contendo essas datas, excluindo a última data da série temporal original.
                """
            )

            st.image('assets/img/Python_Fig_11.png', caption='Código mostrando funções para prever os próximos pontos da série temporal e gerar datas correspondentes', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                No trecho abaixo de código define 15 dias a serem previstos (**num_prediction = 15**) e, em seguida, chama as funções **:gray[`predict()`]** e **:grey[`predict_dates()`]** para realizar as previsões e gerar as datas correspondentes.\n
                A função **:gray[`predict()`]** utiliza o modelo LSTM previamente treinado (*model_lstm*) para prever os próximos pontos da série temporal. Essas previsões são armazenadas na variável forecast.\n
                A função **:gray[`predict_dates()`]** é responsável por gerar as datas correspondentes aos próximos dias previstos. Ela utiliza a última data disponível na série temporal original como referência e cria uma lista de datas para os próximos dias. As datas geradas são armazenadas na variável *forecast_dates*.\n
                Dessa forma, ao final dessas operações, *forecast* contém as previsões dos próximos pontos da série temporal e *forecast_dates* contém as datas correspondentes a essas previsões.
                """
            )

            st.image('assets/img/Python_Fig_12.png', caption='Definição do número de dias previstos e geração das previsões, utilizando as funções predict() e predict_dates()', use_column_width=True, output_format='auto')
 
            st.subheader(":orange[Gerando e Visualizando a Previsão do Preço do Petróleo com o Modelo LSTM]")

            st.markdown(
                """
                Por fim, é gerado um gráfico para mostrar os dados da previsão.\n
                **Preparação dos dados para plotagem:**\n
                :one: Uma data de corte (*data_corte_grafico_lstm*) é definida como **2023-01-01**.\n
                :two: Os dados históricos são filtrados para incluir apenas os registros após a data de corte.\n
                :three: Os dados filtrados são armazenados em um novo DataFrame chamado *df_grafico_lstm*.\n
                **Criação da descrição dos resultados:**\n
                Uma string descritiva é montada incluindo as métricas de desempenho do modelo LSTM, como R², MSE, MAE, MAPE e RMSE.\n
                **Configuração do gráfico:**\n
                O título do gráfico (*titulo_grafico*) é definido como **"Modelo LSTM - Previsão preço do Petróleo"**.\n
                **Duas linhas são plotadas no gráfico:**\n
                A primeira linha (*trace1*) representa os dados históricos do preço do petróleo do DataFrame *df_grafico_lstm*.\n
                A segunda linha (*trace2*) representa a previsão obtida do modelo LSTM, com base nas datas geradas anteriormente (*forecast_dates*) e nas previsões (*forecast*).\n
                O layout do gráfico é configurado com os títulos dos eixos **x** e **y**, bem como a posição da legenda e uma anotação com a descrição dos resultados.\n
                A seguir, o código final usado para prever o preço do petróleo com o modelo LSTM.
                """
            )

            st.image('assets/img/Python_Fig_13.png', caption='Código para plotar a previsão do preço do petróleo usando o modelo LSTM, com métricas de desempenho e dados históricos', use_column_width=True, output_format='auto')
 
            st.markdown(
                """
                Segue abaixo a visualização do gráfico gerado com a previsão do preço do petróleo.
                """
            )

            st.image('assets/img/Python_Fig_14.png', caption='Visualização gráfica com a previsão do preço do petróleo', use_column_width=True, output_format='auto')
 