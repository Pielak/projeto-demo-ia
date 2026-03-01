from pydantic import BaseModel, EmailStr
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    telefone: Optional[str] = None
    ativo: bool = True
