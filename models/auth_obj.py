from pydantic import BaseModel


class AuthObj(BaseModel):
    email: str
    password: str
    confirm_password: str
