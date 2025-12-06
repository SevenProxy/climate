class AppError:
    NOT_ELEMENT = ("E001", "Não foi possível ler elemento html.") 
    INVALID_URL = ("E002", "URL inválida.")
    INVALID_STATUS = ("E003", "Requisição não foi bem efetuada.")
    CONNECTION_FALIED = ("004", "Conexão não foi efetuada.")
    CHANNEL_ERROR = ("005", "Error ao enviar queue.")

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
