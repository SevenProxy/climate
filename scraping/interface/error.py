from typing import Optional, Any
from enum import Enum, auto

class AppError:
    NOT_ELEMENT = ("E001", "Não foi possível ler elemento html.") 
    INVALID_URL = ("E002", "URL inválida.")
    INVALID_STATUS = ("E003", "Requisição não foi bem efetuada.")

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
