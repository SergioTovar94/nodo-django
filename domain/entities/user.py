"""Entidad de dominio User."""

from datetime import datetime

class User:
    """
    Entidad de dominio que representa un usuario del sistema.

    Attributes:
        id (int): Identificador único del usuario.
        name (str): Nombre del usuario.
        email (str): Correo electrónico del usuario.
        password_hash (str): Contraseña en formato hash.
        created_at (datetime): Fecha de creación del usuario.
    """
    def __init__(
            self,
            id: int,
            name: str,
            email: str,
            password_hash: str,
            created_at: datetime
            ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
