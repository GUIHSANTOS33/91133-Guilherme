from flask import Blueprint, jsonify
import sqlite3

listagem_bp = Blueprint('listagem', __name__)

@listagem_bp.route('/api/listar', methods=['GET'])
def listar():
    conn = sqlite3.connect('amigos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome FROM amigos')
    amigos = [linha[0] for linha in cursor.fetchall()]
    conn.close()
    return jsonify(amigos)