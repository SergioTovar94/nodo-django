"""Caso de uso de craeción de usuario"""
from domain.entities.user import User

class CreateUser:
    "Clase de creación de usuario"
    def __init__(self, repository):
        self.repository = repository

    def execute(self, name, email, password_hash):
        """"Método de creación"""
        user = User(
            id = None,
            name = name,
            email = email,
            password_hash = password_hash,
            created_at = None            )

        return self.repository.create(user)
