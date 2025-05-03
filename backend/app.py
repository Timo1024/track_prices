from fastapi import FastAPI, HTTPException
import mysql.connector
import os

app = FastAPI(title="Amazon Price Tracker API")

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "price_tracker"),
            password=os.getenv("DB_PASSWORD", "password"),
            database=os.getenv("DB_NAME", "price_tracker_db")
        )
        return connection
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Hello World from Price Tracker API"}

@app.get("/health/db")
async def check_db():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello World from Database' as message")
        result = cursor.fetchone()
        return {"message": result[0]}
    finally:
        conn.close()
