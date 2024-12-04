import streamlit as st
from tabs.tab import TabInterface


class MetodologiaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":gray[Origem e Análise dos Dados]", divider="orange")

            st.markdown(
                """
Prophet é um procedimento para prever dados de séries temporais com base em um modelo aditivo onde tendências não lineares são ajustadas com sazonalidade anual, semanal e diária, além de efeitos de feriados. Ele funciona melhor com séries temporais que têm fortes efeitos sazonais e várias temporadas de dados históricos. Prophet é robusto para dados ausentes e mudanças na tendência, e normalmente lida bem com outliers.
Prophet é um software de código aberto lançado pela equipe Core Data Science do Facebook. Ele está disponível para download no CRAN e no PyPI.
Precisão e Rapidez
O Prophet é utilizado em muitos aplicativos no Facebook para produzir previsões confiáveis para planejamento e definição de metas. Descobrimos que ele tem um desempenho melhor do que qualquer outra abordagem na maioria dos casos. Ajustamos modelos no Stan para que você obtenha previsões em apenas alguns segundos.
Totalmente Automático
Obtenha uma previsão razoável sobre dados confusos sem esforço manual. O Prophet é robusto para outliers, dados ausentes e mudanças drásticas em suas séries temporais.
Previsões Ajustáveis
O procedimento Prophet inclui muitas possibilidades para os usuários ajustarem e refinar as previsões. Você pode usar parâmetros interpretáveis por humanos para melhorar sua previsão adicionando seu conhecimento de domínio.
Disponível em R ou Python
Implementamos o procedimento Prophet em R e Python, mas ambos compartilham o mesmo código Stan subjacente para ajuste. Use qualquer linguagem com a qual você se sinta confortável para obter previsões.
Previsão de Crescimento
Por padrão, o Prophet usa um modelo linear para sua previsão. Ao prever o crescimento, geralmente há um ponto máximo atingível: tamanho total do mercado, tamanho total da população, etc. Isso é chamado de capacidade de suporte, e a previsão deve saturar neste ponto.
O Prophet permite que você faça previsões usando um modelo de tendência de crescimento logístico, com uma capacidade de carga especificada.
Regressores Adicionais
Regressores adicionais podem ser adicionados à parte linear do modelo usando o método add_regressor ou a função correspondente. Uma coluna com o valor do regressor precisará estar presente nos dataframes de ajuste e de previsão. O regressor extra deve ser conhecido tanto para o histórico quanto para datas futuras. Portanto, deve ser algo que tenha valores futuros conhecidos (como nfl_sunday), ou algo que tenha sido previsto separadamente em outro lugar.
Fonte: Prophet no Facebook


                """
            )
            st.markdown(
                """
                Para a análise dos dados, foi utilizado o arquivo Excel como fonte. Com a ajuda do Python, foram construídos gráficos que permitem visualizar a variação do preço do petróleo ao longo do tempo e entender as informações que trabalhadas.
                """
            )
            st.subheader(":orange[Aplicando o modelo LSTM]")
            st.markdown(
                """
                Utilizando o mesmo arquivo Excel contendo os dados históricos do preço do petróleo, aplicamos o modelo LSTM (Long Short-Term Memory) para prever os preços futuros. 

                Para avaliar a performance do modelo e determinar a confiabilidade das previsões, calculamos diversas métricas de desempenho, incluindo:

                - Coeficiente de Determinação (R²)
                - Erro Médio Quadrático (MSE)
                - Erro Médio Absoluto (MAE)
                - Erro Percentual Absoluto Médio (MAPE)
                - Raiz do Erro Médio Quadrático (RMSE)

                Essas métricas nos permitem compreender melhor a precisão do modelo e a qualidade das previsões geradas.

                Segundo o site *Análise Macro*, temos as seguintes definições:

                - **R² Score (Coeficiente de Determinação):** O R² Score mede a proporção da variância na variável dependente que é previsível a partir da variável independente. Valores de R² próximos de 1 indicam um ajuste perfeito do modelo aos dados, enquanto valores próximos de 0 indicam um ajuste pobre. No caso de R², quanto mais próximo de 1, melhor.\n
                - **MSE (Erro Quadrático Médio):** O MSE é a média dos quadrados dos erros entre os valores reais e os valores previstos. Ele fornece uma medida da dispersão dos erros. Valores mais baixos de MSE indicam que o modelo tem uma boa capacidade de prever os valores reais.\n
                - **MAE (Erro Médio Absoluto):** O MAE é a média dos valores absolutos dos erros entre os valores reais e os valores previstos. Ele fornece uma medida da magnitude média dos erros do modelo. Valores menores de MAE indicam que o modelo tem uma boa capacidade de prever os valores reais.\n
                - **MAPE (Erro Percentual Absoluto Médio):** O MAPE é a média dos valores absolutos dos erros percentuais entre os valores reais e os valores previstos, expressa como uma porcentagem do valor real. Ele fornece uma medida da precisão percentual média das previsões. Valores menores de MAPE indicam que o modelo tem uma boa precisão em suas previsões.\n
                - **RMSE (Raiz do Erro Quadrático Médio):** O RMSE é a raiz quadrada do MSE e fornece uma medida da dispersão dos erros em unidades da variável de interesse. Assim como o MSE, valores mais baixos de RMSE indicam que o modelo tem uma boa capacidade de prever os valores reais.
                """
            )
            st.subheader(":orange[Google Colab]")
            st.markdown(
               """
               Utilizamos o Google Colab para executar o código Python e realizar a análise dos dados do preço do petróleo. O Google Colab é uma plataforma gratuita oferecida pelo Google, acessível a qualquer usuário que possua uma conta Google.\n
               Esta ferramenta permite a execução de códigos Python em servidores da própria Google, facilitando o desenvolvimento e a execução de projetos de análise de dados e aprendizado de máquina sem a necessidade de configuração de um ambiente local.\n
               Além disso, o Google Colab oferece acesso a poderosos recursos de computação, incluindo GPUs, o que pode acelerar significativamente o processamento de dados e a execução de modelos complexos. Essa flexibilidade e acessibilidade tornam o Colab uma escolha ideal para a análise de grandes conjuntos de dados, como os históricos de preços do petróleo.
               """
            )
            #st.image('assets/img/Interface_Colab.png', caption='Interface do usuário do Google Colab')