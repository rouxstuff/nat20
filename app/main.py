# O __init__.py vazio só avisa ao Python que app é um pacote.
# uvicorn app.main:app --reload roda o codigo (reload reinicia o servidor sempre que o arquivo é salvo)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Nat20")

@app.get("/")
def root():
    return {"message": "Welcome to Nat20!"}

@app.get("/about")
def about():
    return{"app": "Nato20", "version":"0.1"}

characters = [
    {"id": 1, "name": "Aria", "char_class": "Mago", "Level": 3},
    {"id": 2, "name": "Thorin", "char_class": "Guerreiro", "Level": 5},
    {"id": 3, "name": "Lyra", "char_class": "Ladino", "Level": 2},
]

class CharacterCreate(BaseModel):
    name : str
    char_class: str
    level: int = 1

@app.get("/characters")
def list_chatacters(char_class: str | None = None, lvl_min: int = 1):
    result = characters
    if char_class is not None:
        result = [c for c in result if c["Class"].lower() == char_class.lower()]
    result = [c for c in result if c["Level"] >= lvl_min]
    return result

def find_character(character_id: int) -> dict:
    for c in characters:
        if c["id"] == character_id:
            return c
    raise HTTPException(status_code=404, detail="Character not found.")

@app.get("/characters/{character_id}")
def get_character(character_id: int):
    return find_character(character_id)           

# create character
@app.post("/characters", status_code=201)
def create_character(data: CharacterCreate):
    new_id = max((c["id"] for c in characters), default=0) +1
    character = {"id": new_id, **data.model_dump()}
    characters.append(character)
    return character

# delete character
@app.delete("/characters/{character_id}", status_code=204)
def delete_character(character_id: int):
    character = find_character(character_id)
    characters.remove(character)

# update character
class CharacterUpdate(BaseModel):
    name: str | None = None
    char_class: str | None = None
    level: int | None = None

@app.patch("/characters/{character_id}")
def update_character(character_id: int, data: CharacterUpdate):
    character = find_character(character_id)
    changes = data.model_dump(exclude_unset=True)
    # TODO: copie cada item de `changes` para `character`
    return character