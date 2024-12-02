import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Conclusão | Tech Challenge 4 | FIAP", layout='wide')
output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.header(":orange[Conclusão]")

    st.subheader(":gray[Análise dos Resultados e Eficácia do Modelo LSTM na Previsão do Preço do Petróleo]", divider="orange")
    st.markdown(
        """
        Dos resultados obtidos, observamos um R² de 86%, o que indica que o modelo está acertando aproximadamente 86% das previsões realizadas. Esse valor é considerado alto, pois está próximo de 100%, sugerindo que o modelo possui uma capacidade significativa de explicar a variabilidade nos dados e de fazer previsões precisas do preço do petróleo. Além disso, temos valores de MSE, MAE e RMSE próximos de zero, o que é bom. Essas métricas indicam que as previsões do modelo têm uma dispersão muito baixa em relação aos valores reais, o que confirma a sua eficácia na previsão do preço do petróleo. Em suma, os resultados obtidos destacam a robustez e a precisão do modelo na tarefa de prever o preço do petróleo com base nos dados fornecidos.
        """
    )

    st.subheader(":gray[Impacto Prático]", divider="orange")
    st.markdown(
        """
        Os resultados obtidos com o modelo LSTM têm um impacto significativo no contexto prático da tomada de decisões no mercado de petróleo. Uma previsão precisa do preço do petróleo é crucial para uma variedade de setores, incluindo finanças, energia e comércio internacional. Com base nos resultados deste estudo, os tomadores de decisão podem tomar medidas mais informadas para mitigar riscos, otimizar investimentos e planejar estratégias de negócios.
        """
    )

    st.subheader(":gray[Aprimoramentos Futuros]", divider="orange")
    st.markdown(
        """
        Embora os resultados até agora sejam promissores, há espaço para aprimoramentos adicionais no modelo LSTM. Algumas áreas de aprimoramento futuro podem incluir:\n
        **1. Incorporação de Mais Dados:** O desempenho do modelo pode ser melhorado pela inclusão de uma gama mais ampla de dados, como dados macroeconômicos, indicadores geopolíticos e informações sobre a demanda global por petróleo.\n
        **2. Otimização de Parâmetros:** A otimização dos hiperparâmetros do modelo LSTM pode ajudar a melhorar ainda mais sua precisão e generalização.\n
        **3. Implementação de Técnicas de Pós-processamento:** Técnicas de pós-processamento, como ensemble learning ou técnicas de correção de viés, podem ser aplicadas para melhorar a robustez e a estabilidade das previsões do modelo.\n
        Essas sugestões de aprimoramentos futuros podem ajudar a aprimorar ainda mais a capacidade do modelo LSTM de prever o preço do petróleo e ampliar seu impacto prático em cenários do mundo real.  
        """
    )