# import bibliotecas
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib

### Instancia do flask
app = Flask(__name__)

# Carregamento do modelos preditivo salvo
model = joblib.load('Modelo_Treinado.pkl')

# Criando rota de aplicacao / configurando end point
@app.route('/predict', methods=['POST'])
def resposta_IA():
    # receber os dados em formato JSON
    data = request.get_json(force=True)

    #Converte esses dados em um dataframe
    df = pd.DataFrame([data])

    #tratamento de dados / garantindo que os dados estejam como float
    df = df.astype(float)

    # Faz as predicoes
    prediction = model.predict(df)
    print("Predição:" , prediction)

    # Estrutura Json
    output = {
        "prediction" : prediction.tolist() #converte o ndarray em uma lista
    }

    # Retornar ao usuario um json de output
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
