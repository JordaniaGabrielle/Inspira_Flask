import os
import sqlite3
import random
from flask import Flask, Response, render_template
import json

app = Flask(__name__)

caminho_banco = os.path.join(os.path.dirname(__file__), '..', 'frases.db')

# Função para gerar frase aleatoria 
def frase_aleatoria():
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()

    # Seleciona todas as frases do banco de dados
    cursor.execute("SELECT texto, autor FROM frases")
    # Pega todas as frases como lista de tuplas
    frases = cursor.fetchall()  
    conn.close()

    if frases:
        frase = random.choice(frases)
        # Retorna um dicionário com a frase e o autor
        return {"frase": frase[0], "autor": frase[1]} 
    else:
        # Caso o banco esteja vazio
        return {"frase": "Nenhuma frase encontrada.", "autor": "Sistema"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frase')
def frase():
    resultado = frase_aleatoria() 
    # Retorna o dicionário como resposta JSON formatada
    return Response(json.dumps(resultado, ensure_ascii=False), mimetype='application/json')
if __name__ == '__main__':
    app.run(debug=True)  # Roda o servidor em modo debug (mostra erros no navegador)