import streamlit as st
from tabs.tab import TabInterface


class IntroTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':orange[Analisando o Mercado de Petróleo]', divider='rainbow')
            st.markdown('''
            O mercado de petróleo é um dos mais dinâmicos e complexos do mundo, com uma grande influência sobre a economia global. Esse mercado envolve a produção, refino, comercialização e consumo de petróleo bruto, que é a principal fonte de energia para diversos setores, como transporte, indústria e geração de eletricidade. Além disso, o petróleo é utilizado na fabricação de uma ampla gama de produtos derivados, como plásticos, fertilizantes e medicamentos.\n
            A dinâmica do mercado de petróleo é fortemente impactada por fatores geopolíticos, econômicos e tecnológicos. Países produtores, como Arábia Saudita, Rússia e Estados Unidos, têm um papel central na definição dos preços do petróleo. O preço do barril de petróleo é, em grande parte, determinado pela oferta e demanda, mas também sofre influência de eventos políticos, como conflitos armados, sanções econômicas e mudanças nas políticas energéticas.\n
            Alterar - "O presente artigo apresenta quatro insights fundamentais que delineiam a variação do preço do petróleo, desde fatores geopolíticos até avanços tecnológicos. Ao explorar esses insights, mergulharemos em um universo complexo e interconectado, onde geopolítica, crises econômicas, demanda energética e inovações tecnológicas convergem para moldar o panorama do mercado do petróleo.\n
            A análise detalhada desses insights não apenas oferece uma compreensão mais profunda das forças que impulsionam as flutuações do preço do petróleo, mas também fornece um guia para tomar decisões estratégicas informadas. Ao longo deste artigo, examinaremos cada insight com exemplos concretos e destacaremos sua relevância no contexto do mercado global de energia.\n
            Portanto, prepare-se para uma jornada pela geopolítica, crises econômicas, demanda energética e inovações tecnológicas, enquanto desvendamos os mistérios por trás das oscilações do preço do petróleo e exploramos as implicações desses insights para o futuro do mercado energético global."
            ''')
           
            #st.image('assets/img/oil-and-gas.jpg', caption='Extração de petróleo: alimentando o mundo com energia', use_column_width=True, output_format='auto')
