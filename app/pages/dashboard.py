import altair as alt
import pandas as pd
import streamlit as st
import utilidades as ut
import os

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


# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    # Diretório base: local do arquivo dashboard.py
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o arquivo CSV relativo ao arquivo dashboard.py
    csv_path = os.path.join(base_dir, '..', '..', 'bases', 'df_ipea_dash.csv')

    # Carregar o arquivo CSV
    df = pd.read_csv(csv_path)
    return df

df = load_data()

# Show a slider widget with the years using `st.slider`.
Ano = st.slider("Anos", 1987, 2006, (2004, 2024))

Produtos = df.Produto.unique()
# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df['Produto'].isin(Produtos)) & (df["Ano"].between(Ano[0], Ano[1]))]
df_reshaped = df_filtered.pivot_table(
    index="Ano", values=["Média","Mínima","Máxima","Variação_Média"], aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="Ano", ascending=False)

# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"Ano": st.column_config.TextColumn("Ano")},
)

df_reshaped = df_reshaped[['Média','Mínima','Máxima']]
# Display the data as an Altair chart using `st.altair_chart`.
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="Ano", var_name="Produto", value_name="1"
)

chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("Ano:N", title="Anos"),
        y=alt.Y("1:Q", title="Preço do Barril de Petróleo ($)"),
        color="Produto:N",
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)

st.markdown('---')

if st.button('Prever'):
# URL da página do ipeadata
    url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"

# Chame a função e obtenha o DataFrame
    df_dados = ut.extrair_dados_ipeadata(url)

    df_ipea = ut.processar_dados(df_dados)

    df_prophet = ut.filtrar_dados_prophet(df_ipea,1)

    treino, teste = ut.dividir_treino_teste(df_ipea, 10)

    qtd_dias_prev = 3

    for dia in range(qtd_dias_prev):
        teste_f = teste
        novo_registro = {
            "ds": ut.acrescentar_um_dia(teste_f.iloc[-1]['ds']),
            "y": 0,
            "open": teste_f.iloc[-1]['y']
        }

        teste_f = ut.adicionar_registro(teste_f, novo_registro)

        predict, forecast = ut.utilizar_prophet(treino,teste_f)
    
        novo_registro = {
            "ds": teste_f.iloc[-1]['ds'],
            "y": round(predict.iloc[-1]['yhat'],2),
            "open": teste.iloc[-1]['y']
        }

        teste =  ut.adicionar_registro(teste, novo_registro)

        


    # Título do aplicativo
    st.title("Análise da Série Temporal")

    st.write(teste.tail(10))
    st.write(predict)