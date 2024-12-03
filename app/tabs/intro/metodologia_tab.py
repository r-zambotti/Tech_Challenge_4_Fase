import streamlit as st
from tabs.tab import TabInterface

class MetodologiaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':orange[Ferramentas e Metodologia]', divider='rainbow')
            st.markdown('''
                        <p style="font-size: 16px"><br>        
                        <b>Para o desenvolvimento das bases de dados, focando na criação de insights, criar dashboard interativos e desenvolver previsões futuras a respeito do valor do 
                        barril do petróleo (forecasting), utilizamos as seguintes ferramentas:</b>
            ''', unsafe_allow_html=True)       

            st.subheader(":gray[Python]")            
            st.markdown('''
                        <p style="font-size: 16px"><br>        
                        <b>Python é uma linguagem de programação de alto nível amplamente utilizada devido à sua simplicidade e versatilidade. 
                        Extremamente utilizada na área de data analytics, é considerada uma das linguagens mais utilizada em todo o mundo.</b>
            ''', unsafe_allow_html=True)       

            st.subheader(":gray[Streamlit]")            
            st.markdown('''
                        <p style="font-size: 16px"><br>        
                        <b>Streamlit é uma ferramenta em Python usada para criar aplicativos interativos de visualização de dados e machine learning. 
                        É famosa pela facilidade em exibir e demonstrar gráficos e na criação de dashboard.</b>
            ''', unsafe_allow_html=True)   

            st.subheader(":gray[.Git e GitHub]")            
            st.markdown('''
                        <p style="font-size: 16px"><br>        
                        <b>O .Git é um sistema de controle de versão distribuído que permite rastrear alterações em arquivos e colaborar em projetos de softwar.
                        Já o GitHub é uma plataforma baseada em nuvem que utiliza Git para hospedar repositórios. Muito importante no ambiente de desenvolvimento, já que permite um controle
                        do código fonte da aplicação.</b>
            ''', unsafe_allow_html=True)

            st.subheader(":gray[Google Colab e Jupyter notebook no VSCode]")            
            st.markdown('''
                        <p style="font-size: 16px"><br>        
                        <b>O Google Colab é uma plataforma baseada na nuvem que permite criar e executar notebooks Jupyte, facilitando a interação e descartando a necessidade de instalar ferramentas no computador local.
                        Em complemento, temos o Visual Studio Code (VSCode) permite trabalhar com notebooks Jupyter localmente, integrando-o com o ambiente de desenvolvimento do editor.</b>
            ''', unsafe_allow_html=True)                                