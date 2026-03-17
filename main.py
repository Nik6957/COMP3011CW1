from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Reward Program API"}

@app.post("/rewards")
def create_reward(name: str, points: int):
    return {"status": "success", "added": name, "points": points}