import streamlit as st

from paginas.analise import Analise
from paginas.dashboard import Dashboard
from paginas.conclusao import Conclusao
from paginas.referencias import Referencias
from paginas.intro import Home

import warnings

warnings.filterwarnings("ignore")

st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


PAGES = {
    "🏠 Home": Home,
    ":chart_with_upwards_trend: Análise": Analise,
    "💻 Dashboard": Dashboard,
    ":white_check_mark: Conclusão": Conclusao,
    "📖 Referências": Referencias
}

st.sidebar.title("Menu")
selection = st.sidebar.radio("Escolha uma opção", list(PAGES.keys()),label_visibility="collapsed")

page = PAGES[selection]()
page.render()  # Chamar o método render() da classe correspondente

with st.sidebar:
        st.divider()
        
        st.subheader("Guia de Instalação:")

        #Passo 1: Criação e ativação do ambiente virtual
        st.markdown("**1º** Crie e ative um ambiente virtual:")

        st.markdown("Para Windows, use:")
        st.code("venv\\Scripts\\activate", language="shell")

        st.markdown("**2º** Instale as bibliotecas com as versões corretas:")
        st.code("pip install -r requirements.txt", language="shell")

        # Passo 3: Execução do aplicativo
        st.markdown("**3º** Execute o aplicativo:")
        st.code("streamlit run main.py", language="shell")