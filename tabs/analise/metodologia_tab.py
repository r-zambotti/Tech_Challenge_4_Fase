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
Prophet é um procedimento para prever dados de séries temporais com base em um modelo aditivo onde tendências não lineares são ajustadas com sazonalidade anual, semanal e diária, além de efeitos de feriados. Ele funciona melhor com séries temporais que têm fortes efeitos sazonais e várias temporadas de dados históricos. Prophet é robusto para dados ausentes e mudanças na tendência, e normalmente lida bem com outliers. Prophet é um software de código aberto lançado pela equipe Core Data Science do Facebook. Ele está disponível para download no CRAN e no PyPI.

Precisão e Rapidez
O Prophet é utilizado em muitos aplicativos no Facebook para produzir previsões confiáveis para planejamento e definição de metas. Descobrimos que ele tem um desempenho melhor do que qualquer outra abordagem na maioria dos casos. Ajustamos modelos no Stan para que você obtenha previsões em apenas alguns segundos.

Totalmente Automático
Obtenha uma previsão razoável sobre dados confusos sem esforço manual. O Prophet é robusto para outliers, dados ausentes e mudanças drásticas em suas séries temporais.

Previsões Ajustáveis
O procedimento Prophet inclui muitas possibilidades para os usuários ajustarem e refinar as previsões. Você pode usar parâmetros interpretáveis por humanos para melhorar sua previsão adicionando seu conhecimento de domínio.

Disponível em R ou Python
Implementamos o procedimento Prophet em R e Python, mas ambos compartilham o mesmo código Stan subjacente para ajuste. Use qualquer linguagem com a qual você se sinta confortável para obter previsões.

Previsão de Crescimento
Por padrão, o Prophet usa um modelo linear para sua previsão. Ao prever o crescimento, geralmente há um ponto máximo atingível: tamanho total do mercado, tamanho total da população, etc. Isso é chamado de capacidade de suporte, e a previsão deve saturar neste ponto. O Prophet permite que você faça previsões usando um modelo de tendência de crescimento logístico, com uma capacidade de carga especificada.

Regressores Adicionais
Regressores adicionais podem ser adicionados à parte linear do modelo usando o método add_regressor ou a função correspondente. Uma coluna com o valor do regressor precisará estar presente nos dataframes de ajuste e de previsão. O regressor extra deve ser conhecido tanto para o histórico quanto para datas futuras. Portanto, deve ser algo que tenha valores futuros conhecidos (como nfl_sunday), ou algo que tenha sido previsto separadamente em outro lugar.

Fonte: Prophet no Facebook


                """
            )
          
            
            st.subheader(":orange[Google Colab]")
            st.markdown(
               """
Para a execução do código Python e a análise dos dados de preços do petróleo, utilizamos o Google Colab. Esta é uma plataforma gratuita disponibilizada pelo Google, acessível a qualquer usuário com uma conta Google.

O Google Colab possibilita a execução de códigos Python em servidores da Google, simplificando o desenvolvimento e a execução de projetos de análise de dados e aprendizado de máquina, sem a necessidade de configurar um ambiente local.

Além disso, o Google Colab proporciona acesso a poderosos recursos computacionais, incluindo GPUs, que podem acelerar significativamente o processamento de dados e a execução de modelos complexos. Essa flexibilidade e acessibilidade tornam o Colab uma ferramenta ideal para a análise de grandes conjuntos de dados, como os históricos de preços do petróleo.
               """
            )
            #st.image('assets/img/Interface_Colab.png', caption='Interface do usuário do Google Colab')