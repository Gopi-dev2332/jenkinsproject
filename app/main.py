from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from FastAPI! with sungjinwhoo and tony stark and Igris"}


@app.get("/about")
def about():
    return {
        "project": "FastAPI Jenkins Demo",
        "status": "Running"
    }
