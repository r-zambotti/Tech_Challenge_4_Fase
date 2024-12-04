import streamlit as st

class Referencias:
    def render(self):
        with st.container():
            st.header(':orange[Referências bibliográficas]', divider="orange")

            st.markdown(''' 
                        1) IPEA. Disponível em: http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view Acesso em 03/12/2024.

                        2) Streamlit. Streamlit Documentation. Disponível em: https://docs.streamlit.io/. 03/12/2024.

                        3) Prophet. Site oficial. Disponível em: https://facebook.github.io/prophet. Acesso em 03/12/2024.    

                        4) G1. O ano em que o petróleo enlouqueceu o mercado. Disponível em: https://g1.globo.com/Noticias/Economia_Negocios/0,,MUL940136-9356,00-O+ANO+EM+QUE+O+PETROLEO+ENLOUQUECEU+O+MERCADO.html#:~:text=LONDRES%2C%2031%20dez%202008%20(AFP)%20-%20O%20mercado,precedente%2C%20que%20pode%20originar%20graves%20problemas%20de%20abastecimento. Acesso em: 26 nov. 2024.
                        
                        5) G1. O que explica o tombo do preço do petróleo e quais os seus efeitos. Disponível em: https://g1.globo.com/economia/noticia/2020/03/09/o-que-explica-o-tombo-do-preco-do-petroleo-e-quais-os-seus-efeitos.ghtml. Acesso em: 13 nov. 2024.
                        
                        6) UOL Economia. Preço do petróleo dispara com guerra na Ucrânia e aumenta temor de crise mundial. Disponível em: https://economia.uol.com.br/cotacoes/noticias/redacao/2022/03/09/preco-do-petroleo-guerra-na-ucrania.htm. Acesso em: 10 nov. 2024.

            ''')