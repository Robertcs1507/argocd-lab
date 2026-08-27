from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres-postgresql.database.svc.cluster.local")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "AppLab2026")

@app.route("/")
def home():
    return jsonify({"status": "backend python funcionando"})

@app.route("/mensagens")
def mensagens():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cur = conn.cursor()
    cur.execute("SELECT id, mensagem FROM mensagens ORDER BY id")
    dados = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {"id": linha[0], "mensagem": linha[1]}
        for linha in dados
    ])

app.run(host="0.0.0.0", port=5000)
