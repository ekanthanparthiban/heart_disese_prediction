import pickle
from fastapi import FastAPI
import uvicorn

# Initialize FastAPI app
app = FastAPI()

@app.get("/ping")
async def ping():
    return "ping me"

with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
