import streamlit as st
from tabs.analise.modelo_mlearning_tab import LSTMTab
from tabs.analise.metodologia_tab import MetodologiaTab
from tabs.analise.resultados_tab import ResultadosTab
from util.layout import output_layout

st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.header(":orange[Análise e Insights]")

    tab0, tab1, tab2 = st.tabs(
        tabs=[
            "Long Short-Term Memory Networks (LSTM)",
            "Metodologia",
            "Resultados"
        ]
    )

    LSTMTab(tab0)
    MetodologiaTab(tab1)
    ResultadosTab(tab2)
     
