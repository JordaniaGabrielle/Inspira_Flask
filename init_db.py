import sqlite3
import json

conn = sqlite3.connect('frases.db')
# cursor é o "controlador" que executa comandos SQL no banco
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS frases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL UNIQUE,
    autor TEXT
)
''')

with open('frases.json', 'r', encoding='utf-8') as arquivo_aberto:
    frases = json.load(arquivo_aberto)

for i in frases:
    autor = i.get('autor') or "Desconhecido"
    try:
        cursor.execute("INSERT INTO frases (texto, autor) VALUES (?, ?)", (i['frase'], autor))
    except sqlite3.IntegrityError:
        
        pass
#salva todas as alterações feitas no banco.
conn.commit()
#fecha a conexão com o banco de dados.
conn.close()


