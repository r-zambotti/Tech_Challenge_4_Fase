import streamlit as st
from util.layout import output_layout

st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.header(":rainbow[Conclusão]")
st.markdown('''
            <p style="font-size: 16px"><br>        
            Este projeto abordou a análise e previsão dos preços históricos do petróleo Brent, com o objetivo de fornecer insights relevantes para a 
            tomada de decisão estratégica e desenvolver uma solução preditiva utilizando ferramentas modernas de Machine Learning<br>
            </p>         
''',unsafe_allow_html=True)

st.subheader(":orange[Pilares de Desenvolvimento]", divider="orange")

st.subheader(":gray[Análise Exploratória de Dados]")
st.markdown('''
            <p style="font-size: 16px"><br>        
            A análise histórica permitiu identificar fatores influenciadores dos preços, como crises econômicas globais, 
            eventos geopolíticos, tensões entre paises e pandemia mundial.<br>
            <br> Foram destacados momentos de impacto significativo, como a crise financeira de 2008 e os efeitos da COVID-19.</br>
            </p>         
''',unsafe_allow_html=True)

st.subheader(":gray[Desenvolvimento do Modelo Preditivo]")
st.markdown('''
            <p style="font-size: 16px"><br>        
            Um modelo de previsão de séries temporais foi implementado para estimar os preços diários do petróleo. 
            As métricas de avaliação indicaram que o modelo é funcional e atende aos requisitos iniciais, apesar das limitações inerentes à volatilidade do mercado.</br>
            <br>Métricas como MAE e MAPE demonstraram que o modelo é confiável dentro do escopo proposto.</br>
            </p>         
''',unsafe_allow_html=True)

st.subheader(":gray[Dashboard Interativo]")
st.markdown('''
            <p style="font-size: 16px"><br>        
            Um dashboard foi desenvolvido para apresentar insights de maneira clara e interativa, 
            conectando os resultados da análise com o storytelling necessário para apoiar decisões estratégicas.</br>
            </p>         
''',unsafe_allow_html=True)

st.subheader(":gray[Plano de Deploy]")
st.markdown('''
            <p style="font-size: 16px"><br>        
            Foi criado um protótipo funcional utilizando o Streamlit, 
            permitindo que as previsões sejam acessadas em um ambiente simples e amigável, pronto para ser utilizado em produção com aprimoramentos futuros.</br>
            </p>         
''',unsafe_allow_html=True)

st.subheader(":orange[Resultados e Contribuições]", divider="orange")
st.markdown('''
            <p style="font-size: 16px"><br>        
            O projeto atendeu aos objetivos iniciais, oferecendo:</br>
            <br>
            - Insights estratégicos baseados nos dados históricos de preços do petróleo.<br>
            - Ferramentas preditivas que permitem estimar valores futuros e ajudam no planejamento estratégico.<br>
            - Uma solução interativa que une storytelling e visualização de dados para facilitar a tomada de decisão.<br>
            </p>         
''',unsafe_allow_html=True)

