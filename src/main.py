from fastapi import FastAPI
from pydantic import BaseModel
from models.character_model import BaseCharacter, Character
from models.user_model import BaseUser

users = {
    "123": {
        "username": "Diego",
        "created_at": "2021-11-01"
    },
    "456": {
        "username": "DazJ",
        "created_at": "2021-11-01"
    }
}

characters = {
    "1": {
        "id": 1,
        "nombre": "Lorem",
        "historia": "Lorem es un bardo que viaja por el mundo en busca de aventuras",
        "nivel": 1,
        "puntos_golpe": 10,
        "fuerza": 10,
        "destreza": 10,
        "constitucion": 10,
        "inteligencia": 10,
        "sabiduria": 10,
        "carisma": 10,
        "experiencia": 0,
        "creado_por": "123",
        "clase": "Bardo",
        "raza": "Elfo"
    },
    "2":{
        "id": 2,
        "nombre": "Ipsum",
        "historia": "Ipsum es un guerrero que busca venganza por la muerte de su familia",
        "nivel": 1,
        "puntos_golpe": 10,
        "fuerza": 10,
        "destreza": 10,
        "constitucion": 10,
        "inteligencia": 10,
        "sabiduria": 10,
        "carisma": 10,
        "experiencia": 0,
        "creado_por": "456",
        "clase": "Guerrero",
        "raza": "Humano"
    }
}

app = FastAPI()

@app.get("/")
async def read_root():
    return "Bienvenido a la API del proyecto final de POO"

@app.post("/auth/register/")
async def create_user(user: BaseUser):
    users[str(len(users) + 1)] = user
    return user

@app.post("/auth/login/")
async def authenticate_user(user: BaseUser):
    for user_id, user_data in users.items():
        if user_data["username"] == user.username:
            return user_data
    return "Usuario no encontrado"

@app.get("/characters/")
async def get_characters():
    return characters

@app.get("/characters/{character_id}")
async def get_character(character_id: str):
    return characters[character_id]

@app.post("/characters/")
async def create_character(character: BaseCharacter):
    characters[str(len(characters) + 1)] = character
    return character