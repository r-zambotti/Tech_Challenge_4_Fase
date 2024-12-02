import streamlit as st
from tabs.tab import TabInterface


class ObjetivoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':orange[Analisando o Mercado de Petróleo: Dashboard Interativo com Storytelling e ML]', divider='rainbow')
            st.markdown('''
                 Introduzir objetivo
            ''')

            #st.image('assets/img/refinaria.png', caption='Refinaria de petróleo: transformando o ouro negro em produtos essenciais')