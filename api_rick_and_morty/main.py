from fastapi import FastAPI

from services import get_characters, get_episodes, get_locations

app = FastAPI()

@app.get("/characters")

def characters():
    return get_characters()

@app.get("/episodes")

def episodes():
    return get_episodes()

@app.get("/locations")

def locations():
    return get_locations()