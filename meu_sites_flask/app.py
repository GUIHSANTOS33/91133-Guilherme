from flask import Flask, render_template
from cadastro.rotas import cadastro_bp
from listagem.rotas import listagem_bp
import sqlite3

app = Flask(__name__)

# Cria o banco e a tabela se não existir
def criar_banco():
    conn = sqlite3.connect('amigos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS amigos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_banco()

# Página principal
@app.route('/')
def home():
    return render_template('index.html')

# Registrar os blueprints
app.register_blueprint(cadastro_bp)
app.register_blueprint(listagem_bp)

if __name__ == '__main__':
    app.run(debug=True)