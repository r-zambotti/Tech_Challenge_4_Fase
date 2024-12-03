import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

# Show the page title and description.
#st.set_page_config(page_title="Movies dataset", page_icon="🎬")
st.title("💻 Dashboard - Análise de Preço do Petróleo")
st.write(
    """
    Dashboard desenvolvido com o objetivo de analisar de forma dinâmica a variação de preços do Barril de Petróleo nos últimos anos\n
    Sendo possível identificar os seguintes itens:\n
    Máxima: Valor máximo do Barril de Petróleo no ano | Média: Valor médio do Barril de Petróleo comparando o valor dia a dia no ano | Minima: Valor minimo do Baril de Petróleo no ano | Variação Média: Comparação da média entre o ano atual e o ano anterior. 
    """
)

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("df_ipea_dash.csv")
    return df

df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
Produtos = st.multiselect(
    "Produto",
    df.Produto.unique(),
    ["Petroleo"],
)

# Show a slider widget with the years using `st.slider`.
Ano = st.slider("Anos", 1987, 2006, (2014, 2024))

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["Produto"].isin(Produtos)) & (df["Ano"].between(Ano[0], Ano[1]))]
df_reshaped = df_filtered.pivot_table(
    index="Ano", values=["Media","Minima","Maxima","Variacao_Media"], aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="Ano", ascending=False)


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"Ano": st.column_config.TextColumn("Ano")},
)

df_reshaped = df_reshaped[['Media','Minima','Maxima']]
# Display the data as an Altair chart using `st.altair_chart`.
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="Ano", var_name="Produto", value_name="1"
)
chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("Ano:N", title="Anos"),
        y=alt.Y("1:Q", title="Preço do Barril de Petróleo (R$)"),
        color="Produto:N",
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)