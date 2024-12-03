import streamlit as st
from tabs.analise.insights_tab import InsightsTab
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
    st.header(":rainbow[Análise e Insights]")

    tab0, tab1, tab2, tab3= st.tabs(
        tabs=[
            "Insights",
            "Long Short-Term Memory Networks (LSTM)",
            "Metodologia",
            "Resultados"
        ]
    )

    InsightsTab(tab0)
    LSTMTab(tab1)
    MetodologiaTab(tab2)
    ResultadosTab(tab3)
     
