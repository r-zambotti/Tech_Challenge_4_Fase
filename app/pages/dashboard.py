import altair as alt
import pandas as pd
import streamlit as st
import utilidades as ut
import os
from datetime import datetime
import plotly.graph_objects as go
from datetime import timedelta

# layout
st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

# Show the page title and description.
st.header("💻:rainbow[ Dashboard - Análise de Preço do Petróleo]")

st.markdown('''
            <p style="font-size: 16px">
            <br>Dashboard desenvolvido com o objetivo de analisar de forma dinâmica a variação de preços do Barril de Petróleo nos últimos anos.
            Sendo possível identificar os seguintes itens:</br>
            <br><b style =>Máxima:</b> Valor máximo do Barril de Petróleo no ano.<br>
            <b style =>Média:</b> Valor médio do Barril de Petróleo comparando o valor dia a dia no ano.<br>
            <b style =>Minima:</b> Valor minimo do Baril de Petróleo no ano<br>
            <b style =>Variação Média:</b> Comparação da média entre o ano atual e o ano anterior.</br>
            </p>         
''',unsafe_allow_html=True)

st.markdown('---')

# Carregar dados do CSV
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '..', '..', 'bases', 'df_ipea_dash.csv')
    df = pd.read_csv(csv_path)
    return df

df = load_data()

# Slider para selecionar os anos
Ano = st.slider("Anos", 1987, 2006, (2004, 2024))

Produtos = df.Produto.unique()
# Filtrar e remodelar o DataFrame
df_filtered = df[(df['Produto'].isin(Produtos)) & (df["Ano"].between(Ano[0], Ano[1]))]
df_reshaped = df_filtered.pivot_table(
    index="Ano", values=["Média","Mínima","Máxima","Variação_Média"], aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="Ano", ascending=False)

# Exibir dados como tabela
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"Ano": st.column_config.TextColumn("Ano")},
)

df_reshaped = df_reshaped[['Média','Mínima','Máxima']]
# Exibir dados como gráfico Altair
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="Ano", var_name="Produto", value_name="Valor"
)

chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("Ano:N", title="Anos"),
        y=alt.Y("Valor:Q", title="Preço do Barril de Petróleo ($)"),
        color="Produto:N",
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)

st.markdown('---')

data_atual = datetime.now().date()
data_maxima = data_atual + timedelta(days=6)

data_selecionada = st.date_input('Selecione a data limite para previsão:', value=data_atual, min_value=data_atual, max_value=data_maxima)
              

# URL da página do ipeadata
url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"

# Extrair e processar dados
df_dados = ut.extrair_dados_ipeadata(url)
df_ipea = ut.processar_dados(df_dados)
df_prophet = ut.filtrar_dados_prophet(df_ipea,1)
treino, teste = ut.dividir_treino_teste(df_ipea, 10)

if st.button('Prever'):
    # Selecionar a última data de teste
    ultimadata = teste.iloc[-1]['ds']
    date_obj = ultimadata.to_pydatetime().date()

    if date_obj < data_selecionada:
        qtd_dias_prev = (data_selecionada - date_obj).days
        if (data_selecionada - data_atual).days >= 7:
            st.info(f'Previsão limitada a 7 dias! \n Refaça sua previsão!')
        else:
            for dia in range(qtd_dias_prev):
                teste_f = teste.copy()
                novo_registro = {
                    "ds": ut.acrescentar_um_dia(teste_f.iloc[-1]['ds']),
                    "y": 0,
                    "open": teste_f.iloc[-1]['y']
                }
                teste_f = ut.adicionar_registro(teste_f, novo_registro)
                predict, forecast = ut.utilizar_prophet(treino, teste_f)
                novo_registro = {
                    "ds": teste_f.iloc[-1]['ds'],
                    "y": round(predict.iloc[-1]['yhat'], 2),
                    "open": teste.iloc[-1]['y']
                }
                teste = ut.adicionar_registro(teste, novo_registro)

            st.title("Tabela de dados")
            predict_renamed = predict.rename(columns={ 'ds': 'Data', 'yhat': 'Previsão' })
            predict_renamed = predict_renamed.set_index('Data')
            st.write(predict_renamed)

            # Filtrar os dados do último ano
            ultimo_ano_inicio = treino['ds'].max() - timedelta(days=30)
            treino_ultimo_ano = treino[treino['ds'] >= ultimo_ano_inicio]

            # Repetir o mesmo para os dados de previsão
            forecast_ultimo_ano = forecast[forecast['ds'] >= ultimo_ano_inicio]


            fig_prophet = go.Figure()

    
            # Dados de treino
            fig_prophet.add_trace(
                go.Scatter(
                    x=treino_ultimo_ano['ds'], 
                    y=treino_ultimo_ano['y'], 
                    mode='markers', 
                    name='Dados de Treino', 
                    marker=dict(color='blue', size=6)
                )
            )

            # Previsão central
            fig_prophet.add_trace(
                go.Scatter(
                    x=forecast_ultimo_ano['ds'], 
                    y=forecast_ultimo_ano['yhat'], 
                    mode='lines', 
                    name='Previsão', 
                    line=dict(color='orange', width=2)
                )
            )

            # Intervalo de confiança
            fig_prophet.add_trace(
                go.Scatter(
                    x=forecast_ultimo_ano['ds'], 
                    y=forecast_ultimo_ano['yhat_lower'], 
                    mode='lines', 
                    line=dict(width=0), 
                    name='Intervalo Inferior', 
                    showlegend=False
                )
            )
            fig_prophet.add_trace(
                go.Scatter(
                    x=forecast_ultimo_ano['ds'], 
                    y=forecast_ultimo_ano['yhat_upper'], 
                    mode='lines', 
                    fill='tonexty', 
                    fillcolor='rgba(211, 211, 211, 0.5)', 
                    line=dict(width=0), 
                    name='Intervalo Superior', 
                    showlegend=False
                )
            )

            # Configurações adicionais do layout
            fig_prophet.update_layout(
                title={'text': 'Previsão Fechamento Ibovespa - 2024 (Prophet)', 'x': 0.5, 'xanchor': 'center'},
                xaxis_title='Data',
                yaxis_title='Fechamento (y)',
                legend_title='Legenda',
                template='plotly_white',
            )

            # Exibe o gráfico
            st.plotly_chart(fig_prophet)
    else:
        st.error(f'Data selecionada é anterior à última data: {ultimadata}!')