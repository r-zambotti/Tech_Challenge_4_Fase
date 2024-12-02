import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Referências | Tech Challenge 4 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header(':orange[Referências bibliográficas]', divider="orange")

    st.markdown('''
    
    1) What is LSTM? Introduction to Long Short-Term Memory. Disponível em: https://www.analyticsvidhya.com/blog/2021/03/introduction-to-long-short-term-memory-lstm/. Acesso em 08/06/2024.
    2) Econometria e Machine Learning. Disponível em: https://analisemacro.com.br/econometria-e-machine-learning/mae-rmse-acc-f1-roc-r2-avaliacao-de-desempenho-de-modelos-preditivos/. Acesso em 08/06/2024.
    3) Investing.com Brasil - Finanças, Câmbio e Investimentos. Disponível em: https://br.investing.com/. Acesso em 15/06/2024.
    4) Crude Oil Prices Today | OilPrice.com. Disponível em: https://oilprice.com/. Acesso em 15/06/2024.
    5) Streamlit. Streamlit Documentation. Disponível em: https://docs.streamlit.io/. Acesso em 11/06/2024.
    6) TensorFlow. Site oficial do TensorFlow. Disponível em: https://www.tensorflow.org/?hl=pt-br. Acesso em 20/06/2024.
    ''')
