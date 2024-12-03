import altair as alt
import pandas as pd
import streamlit as st
# import plotly.graph_objects as go
# from datetime import date, timedelta
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
# from model_lstm.model_lstm import predict, predict_dates, load_model_and_scaler, load_and_process_data, evaluate_lstm_model, create_sequences
# from util.layout import output_layout

# layout
st.set_page_config(layout='centered', 
                   page_title='Tech Challenge 4 - GRUPO 60', 
                   page_icon='⛽', initial_sidebar_state='auto')

# Show the page title and description.
st.title("💻 Dashboard - Análise de Preço do Petróleo")
st.write(
    """
    Dashboard desenvolvido com o objetivo de analisar de forma dinâmica a variação de preços do Barril de Petróleo nos últimos anos\n
    Sendo possível identificar os seguintes itens:\n
    Máxima: Valor máximo do Barril de Petróleo no ano | Média: Valor médio do Barril de Petróleo comparando o valor dia a dia no ano | Minima: Valor minimo do Baril de Petróleo no ano | Variação Média: Comparação da média entre o ano atual e o ano anterior. 
    """
)

st.markdown('---')

# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("df_ipea_dash.csv")
    return df

df = load_data()

# Show a slider widget with the years using `st.slider`.
Ano = st.slider("Anos", 1987, 2006, (2014, 2024))

Produtos = df.Produto.unique()
# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df['Produto'].isin(Produtos)) & (df["Ano"].between(Ano[0], Ano[1]))]
df_reshaped = df_filtered.pivot_table(
    index="Ano", values=["Media","Minima","Maxima","Variacao_Media"], aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="Ano", ascending=False)

# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"Ano": st.column_config.TextColumn("Ano")},
)

df_reshaped = df_reshaped[['Media','Minima','Maxima']]
# Display the data as an Altair chart using `st.altair_chart`.
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="Ano", var_name="Produto", value_name="1"
)

chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("Ano:N", title="Anos"),
        y=alt.Y("1:Q", title="Preço do Barril de Petróleo (R$)"),
        color="Produto:N",
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)

st.markdown('---')

# # Definindo o diretório base onde estão localizados os arquivos
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Configurar caminhos absolutos
# model_path = os.path.join(base_dir, 'model_lstm', 'model_lstm.h5')
# scaler_path = os.path.join(base_dir, 'model_lstm', 'scaler.joblib')
# excel_path = os.path.join(base_dir, 'dataset', 'Petroleo.xlsx')

# try:
#     # Carregar modelo e scaler
#     model_lstm, scaler = load_model_and_scaler(model_path, scaler_path)
# except FileNotFoundError:
#     st.error("Arquivo de modelo ou scaler não encontrado. Verifique os caminhos configurados.")
#     st.stop()
# except Exception as e:
#     st.error(f"Erro ao carregar o modelo e o scaler: {e}")
#     st.stop()

# # Carregar dados e preprocessar
# data_corte = pd.to_datetime('2020-05-03')
# try:
#     df, data_scaled, _ = load_and_process_data(excel_path, data_corte)
# except FileNotFoundError:
#     st.error("Arquivo de dados não encontrado. Verifique o caminho configurado.")
#     st.stop()
# except Exception as e:
#     st.error(f"Erro ao carregar e preprocessar os dados: {e}")
#     st.stop()

# # Definir a data inicial e o limite de dias para a previsão
# DATA_INICIAL = date(2024, 5, 20)
# LIMITE_DIAS = 15

# st.header(":orange[Previsão do Preço do Petróleo]", divider='orange')
# st.info(f"Neste campo, você pode inserir a data desejada para a previsão do preço do barril de petróleo. Para garantir a precisão das previsões, estabelecemos um limite de {LIMITE_DIAS} dias a partir de **20 de maio de 2024**, última data do preço do petróleo na nossa base de dados. Isso assegura que as projeções sejam baseadas em dados recentes e relevantes, proporcionando insights confiáveis sobre a tendência de preço no curto prazo.")

# # Entrada de data pelo usuário
# with st.container():
#     col, _ = st.columns([2, 6])
#     with col:
#         min_date = DATA_INICIAL + timedelta(days=1)
#         max_date = DATA_INICIAL + timedelta(days=LIMITE_DIAS)
#         end_date = st.date_input(
#             "**Escolha a data de previsão:**", 
#             min_value=min_date, 
#             max_value=max_date,
#             value=min_date,
#         )

# # Calcular o número de dias para a previsão com base na data selecionada
# days = (end_date - DATA_INICIAL).days

# sequence_length = 10

# if st.button('Prever'):
#     with st.spinner('Realizando a previsão...'):
#         try:
#             forecast = predict(days, data_scaled, sequence_length)
#             if forecast is None:
#                 st.error("Ocorreu um erro durante a previsão. Verifique os logs para mais detalhes.")
#                 st.stop()
            
#             forecast_dates = predict_dates(days, df)
            
#             train_size = int(len(data_scaled) * 0.8)
#             X_test, y_test = create_sequences(data_scaled[train_size:], sequence_length)
#             r2_lstm, mse_lstm, mae_lstm, mape_lstm, rmse_lstm = evaluate_lstm_model(model_lstm, X_test, y_test, scaler)
            
#             texto_descritivo = f"Performance do Modelo: R² = {round(r2_lstm, 5)}, MSE = {round(mse_lstm, 5)}, MAE = {round(mae_lstm, 5)}, MAPE = {round(mape_lstm, 5)}, RMSE = {round(rmse_lstm, 5)}"
#             titulo_grafico = "Modelo LSTM - Previsão preço do Petróleo"
    
#             trace1 = go.Scatter(x=df['Data'], y=df['Close'], mode='lines', name='Dados Históricos')
#             trace2 = go.Scatter(x=forecast_dates, y=forecast.flatten(), mode='lines', name='Previsão LSTM')
    
#             layout = go.Layout(
#                 title=titulo_grafico,
#                 xaxis={'title': "Data"},
#                 yaxis={'title': "Preço do Petróleo (US$)"},
#                 legend={'x': 0.1, 'y': 0.9},
#                 annotations=[
#                     go.layout.Annotation(
#                         text=texto_descritivo,
#                         align='left',
#                         showarrow=False,
#                         xref='paper',
#                         yref='paper',
#                         x=0,
#                         y=1.1,
#                         bordercolor='black',
#                         borderwidth=1
#                     )
#                 ]
#             )
    
#             fig = go.Figure(data=[trace1, trace2], layout=layout)
#             fig.update_yaxes(range=[60, 110])
#             st.plotly_chart(fig)

#             st.subheader(':gray[Tabela de Previsões de Preço por Data:]', divider='orange')
            
#             # Montando a tabela com os resultados da previsão
#             forecast_df = pd.DataFrame({
#                 "Data": [date.strftime("%Y-%m-%d") for date in forecast_dates],  
#                 "Preço": forecast.flatten().round(2)  
#             })

#             st.write(forecast_df.set_index("Data")) 

#             st.success("Previsão concluída com sucesso! :white_check_mark:")
        
#         except FileNotFoundError as fnf_error:
#             st.error(f"Erro ao encontrar arquivo: {fnf_error}")
        
#         except ValueError as value_error:
#             st.error(f"Erro nos dados: {value_error}")
        
#         except Exception as e:
#             st.error(f"Ocorreu um erro durante a previsão: {e}")