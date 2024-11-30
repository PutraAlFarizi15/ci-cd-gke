from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Fast-API in GKE, waduh kok gk berubah ya?"}