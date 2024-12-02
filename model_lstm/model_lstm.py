import os
import tensorflow as tf
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense

# Função para carregar e preprocessar os dados
def load_and_process_data(excel_path, data_corte):
    df = pd.read_excel(excel_path)
    df = df.rename(columns={'Brent': 'Close'})
    df['Data'] = pd.to_datetime(df['Data'])
    df = df[df['Data'] > data_corte]
    df.reset_index(drop=True, inplace=True)
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(df[['Close']])
    return df, data_scaled, scaler

# Função para criar sequências de dados para entrada no modelo LSTM
def create_sequences(dados, sequence_length):
    X, y = [], []
    for i in range(len(dados) - sequence_length):
        X.append(dados[i:i+sequence_length])
        y.append(dados[i+sequence_length])
    return np.array(X), np.array(y)

# Função para construir o modelo LSTM
def build_lstm_model(sequence_length):
    model_lstm = Sequential([
        LSTM(350, input_shape=(sequence_length, 1)),
        Dense(1)
    ])
    model_lstm.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError())
    return model_lstm

# Função para treinar o modelo LSTM
def train_lstm_model(model, X_train, y_train, epochs, batch_size):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
    return model

# Função para avaliar o modelo LSTM usando métricas de desempenho
def evaluate_lstm_model(model, X_test, y_test, scaler):
    lstm_predictions = model.predict(X_test)
    r2_lstm = r2_score(y_test, lstm_predictions)
    mse_lstm = mean_squared_error(y_test, lstm_predictions)
    mae_lstm = mean_absolute_error(y_test, lstm_predictions)
    mape_lstm = np.mean(np.abs((y_test - lstm_predictions) / y_test)) * 100
    rmse_lstm = np.sqrt(mean_squared_error(y_test, lstm_predictions))
    return r2_lstm, mse_lstm, mae_lstm, mape_lstm, rmse_lstm

# Função para salvar o modelo treinado e scaler
def save_model_and_scaler(model, scaler, model_path, scaler_path):
    model.save(model_path)
    joblib.dump(scaler, scaler_path)

# Função para carregar o modelo salvo e scaler
def load_model_and_scaler(model_path, scaler_path):
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError("Model or scaler file not found.")
    model_lstm = load_model(model_path)
    scaler = joblib.load(scaler_path)
    return model_lstm, scaler

# Função para prever valores futuros com o modelo LSTM
def predict(num_prediction, data_scaled, sequence_length):
    try:
        # Carregar o modelo e o escalador
        model_lstm, scaler = load_model_and_scaler('model_lstm/model_lstm.h5', 'model_lstm/scaler.joblib')
        print("Modelo e escalador carregados com sucesso.")

        if len(data_scaled) < sequence_length:
            raise ValueError("O comprimento dos dados escalados é menor que o comprimento da sequência.")

        prediction_list = list(data_scaled[-sequence_length:])  # Converte para lista
        print(f"Tamanho inicial da lista de previsões: {len(prediction_list)}")

        for _ in range(num_prediction):
            x = np.array(prediction_list[-sequence_length:]).reshape((1, sequence_length, 1))
            out = model_lstm.predict(x)[0][0]
            print(f"Previsão gerada: {out}")
            prediction_list.append([out])  # Adiciona a previsão como lista contendo um único elemento

        # Ajustar o tamanho de prediction_list para considerar as novas previsões
        prediction_list = prediction_list[-num_prediction:]
        print(f"Tamanho da lista de previsões após adicionar novas previsões: {len(prediction_list)}")

        # Desnormalizar as previsões
        prediction_list = scaler.inverse_transform(np.array(prediction_list).reshape(-1, 1))
        print(f"Previsões desnormalizadas: {prediction_list}")

        return prediction_list

    except FileNotFoundError as fnfe:
        print(f"Erro ao carregar o modelo ou escalador: {fnfe}")
    except ValueError as ve:
        print(f"Erro no valor dos dados: {ve}")
    except Exception as e:
        print(f"Erro durante a previsão: {e}")
    return None

# Função para gerar uma lista de datas para as previsões
def predict_dates(num_prediction, data):
    last_date = data['Data'].iloc[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates[1:]

# Função para treinar o modelo LSTM e salvar o modelo e scaler
def train_and_save_lstm_model(excel_path, model_path, scaler_path, data_corte, sequence_length):
    df, data_scaled, scaler = load_and_process_data(excel_path, data_corte)
    train_size = int(len(data_scaled) * 0.8)
    X_train, y_train = create_sequences(data_scaled[:train_size], sequence_length)
    X_test, y_test = create_sequences(data_scaled[train_size:], sequence_length)
    model_lstm = build_lstm_model(sequence_length)
    model_lstm = train_lstm_model(model_lstm, X_train, y_train, epochs=100, batch_size=64)
    r2_lstm, mse_lstm, mae_lstm, mape_lstm, rmse_lstm = evaluate_lstm_model(model_lstm, X_test, y_test, scaler)
    save_model_and_scaler(model_lstm, scaler, model_path, scaler_path)
    
    print(f"R² Score (LSTM): {r2_lstm}")
    print(f"MSE (LSTM): {mse_lstm}")
    print(f"MAE (LSTM): {mae_lstm}")
    print(f"MAPE (LSTM): {mape_lstm}")
    print(f"RMSE (LSTM): {rmse_lstm}")

if __name__ == "__main__":
    # Defina o diretório base como o diretório onde este script está localizado
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construa os caminhos relativos
    excel_path = os.path.join(base_dir, 'dataset', 'Petroleo.xlsx')
    model_path = os.path.join(base_dir, 'model_lstm', 'model_lstm.h5')
    scaler_path = os.path.join(base_dir, 'model_lstm', 'scaler.joblib')
    
    data_corte = pd.to_datetime('2020-05-03')
    sequence_length = 10
    
    # Treinar o modelo LSTM e salvar o modelo e scaler
    train_and_save_lstm_model(excel_path, model_path, scaler_path, data_corte, sequence_length)
