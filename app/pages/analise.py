import streamlit as st
from tabs.analise.insights_tab import InsightsTab
from tabs.analise.metodologia_tab import MetodologiaTab
from tabs.analise.resultados_tab import ResultadosTab

class Analise:
    def render(self):
        st.header(":rainbow[Análise e Insights]")

        tab0, tab1, tab2= st.tabs(
            tabs=[
                "Insights",
                "Metodologia",
                "Resultados"
            ]
        )
        InsightsTab(tab0)
        MetodologiaTab(tab1)
        ResultadosTab(tab2)