from fastapi import FastAPI

app = FastAPI()

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