import streamlit as st
from tabs.tab import TabInterface


class IntroTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':orange[Analisando o Mercado de Petróleo]', divider='rainbow')
            st.markdown ('''
                        <p style="font-size: 16px">
                        <br>O mercado de petróleo é um dos mais dinâmicos e complexos do mundo, com uma grande influência sobre a economia global. 
                        Esse mercado envolve a produção, refino, comercialização e consumo de petróleo bruto, que é a principal fonte de energia para diversos setores, como transporte, indústria e geração de eletricidade. 
                        Além disso, o petróleo é utilizado na fabricação de uma ampla gama de produtos derivados, como plásticos, fertilizantes e medicamentos.</br>
                         
                        <br>A dinâmica do mercado de petróleo é fortemente impactada por fatores geopolíticos, econômicos e tecnológicos. Países produtores, como Arábia Saudita, Rússia e Estados Unidos, têm um papel central na definição dos preços do petróleo. 
                        O preço do barril de petróleo é, em grande parte, determinado pela oferta e demanda, mas também sofre influência de eventos políticos, como conflitos armados, sanções econômicas e mudanças nas políticas energéticas.</br>                                         
            ''',unsafe_allow_html=True) 