from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

# Подключаемся к PostgreSQL (используем переменную окружения из Railway)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

@app.get("/")
def read_root():
    return {"message": "Hello, Railway!"}

@app.get("/api/data")
def get_data():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM drivers;")  # Замените `your_table` на имя таблицы
    data = cur.fetchall()
    conn.close()
    return {"data": data}
