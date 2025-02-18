from pydantic import BaseModel

class BaseUser(BaseModel):
    username: str

class User(BaseUser):
    created_at: str