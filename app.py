#====================================================== BIBLIOTECAS ==================================================

from flask import Flask, render_template, jsonify, json
import sqlite3
import os


app = Flask(__name__, static_folder='static', template_folder='templates')

DB_PACK = os.path.join('rh_database.db')

# ==================================================== Banco de Dados =================================================

def criar_banco():
    conec = sqlite3.connect(DB_PACK)
    conec.row_factory = sqlite3.Row
    return conec

# ==================================================== Front-End =====================================================
@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True, port=8000)
