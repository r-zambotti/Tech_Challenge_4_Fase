import streamlit as st
from tabs.tab import TabInterface


class LSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":gray[Modelo de Machine Learning para Previsão Diária dos Preços do Petróleo]", divider="orange")

            st.markdown(
                """
                Long Short-Term Memory Networks (LSTM) são uma forma avançada de rede neural profunda (deep learning) que se destacam por sua capacidade de preservar e utilizar informações passadas para influenciar previsões futuras. As LSTMs são uma classe especial de redes neurais recorrentes (Recurrent Neural Networks - RNNs), projetadas para superar as limitações das RNNs tradicionais, especialmente em relação à memória de longo prazo. Essas redes foram desenvolvidas por Sepp Hochreiter e Jürgen Schmidhuber.\n
                Para ilustrar o funcionamento das LSTMs, podemos usar a analogia da leitura de um livro. Imagine que você está lendo um livro, passando por cada capítulo sequencialmente. À medida que avança na leitura, você mantém na memória os eventos e detalhes dos capítulos anteriores, o que ajuda a entender e interpretar a narrativa como um todo. As RNNs tradicionais funcionam de maneira semelhante, tentando utilizar a informação de entradas anteriores para influenciar a saída atual. No entanto, elas enfrentam dificuldades para lembrar informações de longas sequências anteriores, limitando sua "memória" a curtos períodos.\n
                Por outro lado, as LSTMs foram projetadas para superar essa limitação. Elas possuem uma arquitetura interna que permite reter informações relevantes por períodos mais longos, sem que estas se percam ao longo do tempo. Voltando à nossa analogia, enquanto uma RNN poderia esquecer detalhes de capítulos lidos há muito tempo, uma LSTM tem a capacidade de lembrar esses capítulos distantes, o que enriquece a análise da história e melhora a precisão das previsões em séries temporais.\n
                Assim, as LSTMs são particularmente eficazes em tarefas onde a memória de longo prazo é crucial, como na modelagem de séries temporais, no processamento de linguagem natural e em muitas outras aplicações que exigem a retenção de informações contextuais ao longo de longas sequências.
            """
            )
            st.subheader(":orange[O que é LSTM?]")
            st.markdown(
                """
                As redes LSTM (Long Short-Term Memory) são um tipo avançado de Redes Neurais Recorrentes (RNNs) amplamente utilizadas no campo do deep learning. Sua principal vantagem é a capacidade de capturar dependências em longos intervalos de tempo, tornando-as ideais para análise e previsão de dados sequenciais.\n
                Ao contrário das redes neurais tradicionais, que processam dados ponto a ponto, as LSTMs são projetadas para lidar com sequências completas de dados. Elas incorporam um mecanismo de feedback em suas conexões, o que lhes permite manter e utilizar informações de entradas passadas para influenciar as saídas futuras. Essa arquitetura permite que as LSTMs processem informações contextuais ao longo de longas sequências, em vez de considerar apenas os pontos individuais de dados.\n
                Essa característica torna as LSTMs extremamente eficazes para entender e prever padrões em dados sequenciais, como séries temporais. Por exemplo, em aplicações de previsão financeira, análise de texto ou reconhecimento de fala, a capacidade das LSTMs de reter e processar informações anteriores é crucial para captar tendências e padrões complexos ao longo do tempo.
            """
            )
            st.subheader(":orange[Entendendo o Funcionamento das Redes LSTM]")
            st.markdown(
                """
                A arquitetura de uma rede LSTM é composta por três componentes fundamentais: **Porta de Esquecimento**, **Porta de Entrada** e **Porta de Saída**. Cada uma dessas portas desempenha um papel crucial no funcionamento do LSTM.\n
                :one: **Porta de Esquecimento:** A primeira etapa no processo do LSTM é decidir quais informações do estado anterior devem ser mantidas e quais devem ser descartadas. Isso é determinado pela porta de esquecimento.\n
                :two: **Porta de Entrada:** Em seguida, o LSTM decide quais informações novas serão armazenadas. A porta de entrada controla a atualização com as informações novas. Ela combina a entrada atual e a memória filtrada pelo estado anterior para determinar o que será adicionado.\n
                :three: **Porta de Saída:** Finalmente, a porta de saída decide qual parte será usada para produzir a saída do LSTM.
            """
            )
            st.image(
                "assets/img/LSTM_Algoritmo.png", 
                caption="Algoritmo LSTM"
            )
            st.markdown(
                """
                Durante um **single-time step** (um único passo de tempo), esse processo cíclico permite que a rede LSTM decida dinamicamente quais informações manter ou esquecer, quais novas informações integrar, e como combinar essas informações para influenciar a saída atual e o estado subsequente. Este mecanismo de gerenciamento de memória é o que permite que as LSTMs mantenham e utilizem informações ao longo de sequências longas, superando as limitações das RNNs tradicionais.
            """
            )