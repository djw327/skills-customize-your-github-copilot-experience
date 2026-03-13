# Starter code for Building REST APIs with FastAPI

# Install FastAPI: pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

# TODO: Add your endpoints here

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment"}

# Run with: uvicorn main:app --reload