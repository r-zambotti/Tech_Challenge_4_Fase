import streamlit as st
from util.layout import output_layout

st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

output_layout()

with st.container():
    st.header(':orange[Referências bibliográficas]', divider="orange")

    st.markdown('''
    
    1) IPEA. Disponível em: http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view Acesso em 03/12/2024.
    2) Streamlit. Streamlit Documentation. Disponível em: https://docs.streamlit.io/. 03/12/2024.
    3) Prophet. Site oficial. Disponível em: https://facebook.github.io/prophet. Acesso em 03/12/2024.
    ''')

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



        