from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Sirventor está en línea!"}

@app.post("/query")
def query_sirventor(data: dict):
    user_input = data.get("query", "")
    response = f"Sirventor dice: {user_input}"
    return {"response": response}
