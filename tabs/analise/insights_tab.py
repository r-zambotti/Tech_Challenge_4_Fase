import streamlit as st
import plotly.express as px
import pandas as pd

from tabs.tab import TabInterface

from util.utils import (normality_test, 
                        create_warning, 
                        create_quote, 
                        create_curiosity, 
                        create_insight, 
                        create_analysis, 
                        insert_image)

class InsightsTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":orange[Selecione um insight]")
            # select one feature to plot with brent
            features_to_plot = ['Eleição brasileira', 'Crise Econômica de 2008', 'Pandemia - Covid-19', 'Guerra na Rússia']           
            selected_feature = st.selectbox('', features_to_plot)
            st.markdown('---')

            # Insight Eleição Brasileira
            if selected_feature == "Eleição brasileira":
                st.subheader(":gray[A Influência das Eleições Presidenciais Brasileiras nos Preços do Petróleo Brent: Uma análise]")

                st.markdown('''
                            <p style="font-size: 16px"><br>        
                            A relação entre eleições presidenciais no Brasil e os preços do petróleo Brent é um tema complexo e multifacetado, sem uma resposta definitiva e linear. 
                            Diversos fatores, tanto internos quanto externos, podem influenciar os preços das commodities energéticas, e as eleições são apenas um deles.<br>
                            </p>         
                ''',unsafe_allow_html=True)

                st.markdown('''
                            <p style="font-size: 16px"><br>
                            Desde a Proclamação da República em 1889, o Brasil teve várias eleições presidenciais. As eleições diretas ocorreram nos seguintes anos: 1891, 1894, 1898, 1902, 1906, 1910, 1914, 1918, 1922, 1926, 1930, 1945, 1950, 1955, 1960, 1989, 1994, 1998, 2002, 2006, 2010, 2014, 2018 e 2022.
                            Para entender melhor essa dinâmica, é preciso considerar alguns pontos:</br>
                            <br>
                            <b style =>- Expectativas de Política Energética:</b> Durante os períodos eleitorais, os candidatos costumam apresentar propostas para o setor de energia, incluindo a política de preços dos combustíveis. Se houver expectativas de mudanças significativas na política energética, isso pode gerar incertezas no mercado e, consequentemente, influenciar os preços do petróleo.<br>
                            <b style =>- Clima de Investimentos:</b> A incerteza política gerada por um processo eleitoral pode afetar o clima de investimentos no país. Se os investidores se mostrarem mais avessos ao risco, podem reduzir seus investimentos em ativos brasileiros, incluindo os relacionados ao setor de petróleo.<br>
                            <b style =>- Fortalecimento ou Desvalorização do Real:</b> As oscilações na taxa de câmbio podem impactar os preços dos combustíveis no Brasil, já que o petróleo é negociado em dólar no mercado internacional. Se o real se desvalorizar, os custos de importação do petróleo aumentam, o que pode pressionar os preços dos combustíveis no mercado interno.<br>
                            <b style =>- Fatores Externos:</b> É importante lembrar que os preços do petróleo são determinados por um conjunto de fatores globais, como a demanda mundial por petróleo, a produção dos países da OPEP, conflitos geopolíticos e eventos climáticos extremos. Esses fatores podem ter um impacto muito maior nos preços do petróleo do que as eleições presidenciais em um único país.<br>
                            <br>
                            Em resumo, embora as eleições presidenciais no Brasil possam influenciar os preços do petróleo Brent, essa influência é geralmente indireta e depende de diversos outros fatores. É difícil isolar o impacto das eleições dos demais fatores que afetam o mercado de petróleo.</br>
                            <br>
                            Abaixo podemos observar como o preço do petróleo se comportou em relação ao ano do período eleitoral com a média dos 3 anos antecedentes.</br>  

                            </p>
                ''', unsafe_allow_html=True)      

                st.markdown('---')

            #Insight Crise Econômica de 2008
            if selected_feature == "Crise Econômica de 2008":
                st.subheader(":gray[Analisando a alta do Petróleo durante a crise de 2008]")
                
                st.markdown('''
                            <p style="font-size: 16px"><br>
                            Analisando a série histórica da base de dados compartilhada pelo IPEA, é possível dimensionar os efeitos da crise econômica de 2008 e o que causou a alta do preço do barril de petróleo, 
                            e como esses dois fatores estão interligados, refletindo a vulnerabilidade dos mercados globais e a instabilidade que pode ser gerada por uma série de fatores interconectados.</br>
                            <br>
                            Ao gerar uma decomposição da série de preço do petróleo nos últimos 20 anos, é possível observar os ruídos e toda a movimentação do valor do petróleo nas últimas duas décadas.</br>
                ''', unsafe_allow_html=True)

                #Inserindo imagem - serie_temporal_2008
                insert_image(image_path = r'assets/img/serie_temporal_2008.png',
                caption = 'Decomposição da Série de Preço do Petróleo (Brent) - 20 anos')

                st.markdown('''
                            <p style="font-size: 16px">
                            <br>Analisando a decomposição da série temporal, observamos que:</br>
                            <b style =>• Tendência:</b> Houve a maior alta no ano de 2008, e a maior queda no ano de 2020;<br>
                            <b style =>• Sazonalidade:</b> A presença de um padrão repetitivo e regular ao longo dos anos. Isso sugere que fatores específicos a cada mês do ano podem influenciar significativamente o desempenho do índice;<br>
                            <b style =>• Ruído:</b> Podemos observar que houve alguns pontos que causaram esses ruídos.<br>
                            <br>Antes de a crise eclodir, os preços do petróleo atingiam níveis elevados. 
                            Entre 2004 e 2008, o barril de petróleo experimentou uma ascensão constante e significativa. Em meados de 2008, 
                            o preço do barril de petróleo Brent, que serve como referência internacional, superou os US$ 140, um patamar histórico.</br>                       
                            </p>
                    ''', unsafe_allow_html=True)  

                #Inserindo imagem - Media_Mensal_2008
                insert_image(image_path = r'assets/img/Media_Mensal_2008.png',
                caption = 'Média Mensal da variação de 2008')

                st.markdown ('''
                            <p style="font-size: 16px">
                            <br>Essa alta foi alimentada por uma combinação de fatores, como o aumento da demanda global, a instabilidade política e geopolítica em regiões-chave produtoras de petróleo, 
                            como o Oriente Médio e a África, contribuiu para a especulação sobre a escassez de oferta e levou os preços a subir.</br>
                            <br>Em setembro de 2008, a crise financeira global eclodiu com a falência do banco Lehman Brothers, que desencadeou uma onda de pânico nos mercados financeiros internacionais. 
                            A crise foi resultado de uma série de fatores, incluindo o colapso do mercado imobiliário nos Estados Unidos, a sobrecarga de dívidas de alto risco e a instabilidade nos sistemas bancários. 
                            A partir desse momento, a economia mundial entrou em uma recessão profunda, o que afetou diretamente o consumo de petróleo.</br>
                            </p>
                    ''',unsafe_allow_html=True)
                
                #Inserindo imagem - Media_Mensal_2008
                insert_image(image_path = r'assets/img/reportagem_crise_2008.jpg',
                source = 'https://g1.globo.com/Noticias/Economia_Negocios/0,,MUL940136-9356,00-O+ANO+EM+QUE+O+PETROLEO+ENLOUQUECEU+O+MERCADO.html#:~:text=LONDRES%2C%2031%20dez%202008%20%28AFP%29%20-%20O%20mercado,precedente%2C%20que%20pode%20originar%20graves%20problemas%20de%20abastecimento.',
                caption = '2008, o ano em que o petróleo enlouqueceu o mercado')

            #Insight Pandemia - Covid 19
            if selected_feature == "Pandemia - Covid-19":
                st.markdown (
                """
                Teste
                """
                )          

            #Insight Guerra na Rússia
            if selected_feature == "Guerra na Rússia":
                st.markdown (
                """
                Teste
                """
                )                     
