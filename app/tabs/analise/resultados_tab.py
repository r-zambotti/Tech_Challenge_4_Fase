import streamlit as st
from tabs.tab import TabInterface


class ResultadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":gray[Tratativa de dados e Analisando as performances do modelo]", divider="orange")

            st.markdown(
                """
                "https://github.com/r-zambotti/Tech_Challenge_4_Fase/blob/main/Notbook/Tech_Challenge_Data_Viz.ipynb" 
                """
            )