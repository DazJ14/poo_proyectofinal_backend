from pydantic import BaseModel

class BaseCharacter(BaseModel):
    nombre: str
    historia: str | None = None
    creado_por: str
    clase: str
    raza: str

class Character(BaseCharacter):
    id: int
    nivel: int = 1
    puntos_golpe: int = 10
    fuerza: int = 10
    destreza: int = 10
    constitucion: int = 10
    inteligencia: int = 10
    sabiduria: int = 10
    carisma: int = 10
    experiencia: int = 0
