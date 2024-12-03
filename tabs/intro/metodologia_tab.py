import streamlit as st
from tabs.tab import TabInterface

class MetodologiaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':orange[Utilização do Streamlit para Estrutura de MVP]', divider='rainbow')
            st.markdown('''
                Adicionar texto de metodologia
            ''')         