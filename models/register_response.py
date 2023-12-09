from pydantic import BaseModel


class RegisterResponse(BaseModel):
    token: str
    email: str
    id: int
