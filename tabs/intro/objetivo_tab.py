import streamlit as st
from tabs.tab import TabInterface


class ObjetivoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':orange[Dashboard Interativo, Storytelling, ML e Insights]', divider='rainbow')
            st.markdown ('''
                        <p style="font-size: 16px">
                        <br>O trabalho objetiva criar dashboard interativo, elaborar insights a respeito de eventos que marcaram a alta e a queda do preço do barril de petróleo
                        e explorar as funcionalidades do Machine Learning, buscando fazer análises futuras e elaborar storystelling dos gráficos desenvolvidos.</br>
                         
                        <br>Como desáfio, um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo para gerar insights relevantes para 
                        tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.</br>     
                                                             
            ''',unsafe_allow_html=True) 