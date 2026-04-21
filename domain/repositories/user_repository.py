"""Archivo de repositorio"""
from abc import ABC, abstractmethod
from domain.entities.user import User

class UserRepository(ABC):
    """Contrato del repositorio User"""
    @abstractmethod
    def create(self, user: User):
        pass
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def get_by_id(self, user_id: int):
        pass
    @abstractmethod
    def update(self, user_id: int):
        pass
    @abstractmethod
    def dalete(self, user_id: int):
        pass
