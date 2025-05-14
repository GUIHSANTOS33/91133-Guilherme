from flask import Blueprint, request, jsonify
import sqlite3

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/api/adicionar', methods=['POST'])
def adicionar():
    dados = request.json
    if not dados or 'nome' not in dados:
        return jsonify({'erro': 'O campo "nome" é obrigatório!'}), 400

    nome = dados['nome']

    conn = sqlite3.connect('amigos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO amigos (nome) VALUES (?)', (nome,))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Amigo adicionado com sucesso!'}), 201