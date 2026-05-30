# ==========================================================
# BIBLIOTECAS
# ==========================================================

from flask import Flask, render_template, jsonify, request, redirect
import sqlite3
import os


# ==========================================================
# CONFIGURAÇÃO DO FLASK
# ==========================================================

app = Flask(__name__, static_folder="static", template_folder="templates")


# ==========================================================
# BANCO DE DADOS
# ==========================================================

DB_PACK = os.path.join("database", "pegueicupom.db")


def criar_banco():
    os.makedirs("database", exist_ok=True)

    conec = sqlite3.connect(DB_PACK)
    conec.row_factory = sqlite3.Row

    return conec


def criar_tabelas():
    conec = criar_banco()
    cursor = conec.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL DEFAULT 'comum'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lojas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            site TEXT,
            logo TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cupons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            desconto TEXT,
            validade TEXT,
            loja_id INTEGER,
            FOREIGN KEY (loja_id) REFERENCES lojas(id)
        )
    """)

    conec.commit()
    conec.close()


criar_tabelas()


# ==========================================================
# ROTAS DO FRONT-END
# ==========================================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login-comum")
def login_comum():
    return render_template("login-comum.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


# ==========================================================
# LOJAS
# ==========================================================

@app.route("/lojas", methods=["GET", "POST"])
def lojas():
    if request.method == "POST":
        nome = request.form["nome"]
        site = request.form["site"]
        logo = request.form["logo"]

        conec = criar_banco()
        cursor = conec.cursor()

        cursor.execute("""
            INSERT INTO lojas (nome, site, logo)
            VALUES (?, ?, ?)
        """, (nome, site, logo))

        conec.commit()
        conec.close()

        return redirect("/lojas")

    conec = criar_banco()
    cursor = conec.cursor()

    cursor.execute("SELECT * FROM lojas ORDER BY id DESC")
    lojas_cadastradas = cursor.fetchall()

    conec.close()

    return render_template("lojas.html", lojas=lojas_cadastradas)


# ==========================================================
# CUPONS
# ==========================================================

@app.route("/cupons")
def cupons():
    return render_template("cupons.html")


# ==========================================================
# ROTA DE TESTE DO BANCO
# ==========================================================

@app.route("/teste-banco")
def teste_banco():
    conec = criar_banco()
    cursor = conec.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()

    conec.close()

    lista_tabelas = [tabela["name"] for tabela in tabelas]

    return jsonify({
        "mensagem": "Banco funcionando corretamente!",
        "tabelas_criadas": lista_tabelas
    })


# ==========================================================
# EXECUÇÃO DO SISTEMA
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True, port=8000)