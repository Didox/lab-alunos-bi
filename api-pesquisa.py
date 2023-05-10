import csv

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensagem': 'Bem vindo a API de pesquisa'})


@app.route('/pesquisa', methods=['OPTIONS'])
def realizar_pesquisa_optionals():
    response = jsonify({'mensagem': 'ok'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

@app.route('/pesquisa', methods=['POST'])
def realizar_pesquisa():
    data = request.get_json()
    email = data['email']
    marca = data['marca']
    cor = data['cor']
    valor = data['valor']
    carro = data['carro']
    salvar_pesquisa(email, marca, cor, valor, carro)
    response = jsonify({'mensagem': 'Pesquisa salva com sucesso!'})
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    
    return response

def salvar_pesquisa(email, marca, cor, valor, carro):
    with open('pesquisas-api.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([email, marca, cor, valor, carro])

if __name__ == '__main__':
    app.run(debug=True)


# print("oi - pessoal")