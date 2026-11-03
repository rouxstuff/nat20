# O __init__.py vazio só avisa ao Python que app é um pacote.
# uvicorn app.main:app --reload roda o codigo (reload reinicia o servidor sempre que o arquivo é salvo)

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Nat20")

@app.get("/")
def root():
    return {"message": "Welcome to Nat20!"}

@app.get("/about")
def about():
    return{"app": "Nato20", "version":"0.1"}

characters = [
    {"id": 1, "Name": "Arya", "Class": "Mage"},
    {"id": 2, "Name": "Logan", "Class": "Warrior"}
]

@app.get("/characters")
def list_chatacters(Class: str | None = None):
    if Class is None:
        return characters
    return [c for c in characters if c["Class"].lower() == Class.lower()]

@app.get("/characters/{character_id}")
def search_character(character_id: int):
    for c in characters:
        if c["id"] == character_id:
            return c
    raise HTTPException(status_code=404, detail="Character not found")            