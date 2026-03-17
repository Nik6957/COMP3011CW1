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
    db.execute('INSERT INTO rewards (name, points) VALUES (?, ?)', (name, points))
    db.commit()
    return {"message": "Points added"}

# Read
@app.get("/rewards")
def read_rewards():
    curent = db.execute('SELECT * FROM rewards')
    return [{"id": row[0], "name": row[1], "points": row[2]} for row in curent.fetchall()]

# Update
@app.put("/rewards/{reward_id}")
def update_reward(reward_id: int, points: int):
    db.execute('UPDATE rewards SET points = ? WHERE id = ?', (points, reward_id))
    db.commit()
    return {"message": "Updated points."}

# Delete
@app.delete("/rewards/{reward_id}")
def delete_reward(reward_id: int):
    db.execute('DELETE FROM rewards WHERE id = ?', (reward_id,))
    db.commit()
    return {"message": "Deleted points"}