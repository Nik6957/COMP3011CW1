from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

def connect_db():
    connect = sqlite3.connect('rewards.db', check_same_thread = False)
    return connect

db = connect_db()
db.execute('CREATE TABLE IF NOT EXISTS rewards (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, points INTEGER)')

# Create
@app.post("/rewards")
def create_reward(name: str, points: int):
    return {"status": "success", "added": name, "points": points}

# Read
@app.get("/")
def read_rewards():
    return {"message": "Reward Program API"}

# Update
# Delete