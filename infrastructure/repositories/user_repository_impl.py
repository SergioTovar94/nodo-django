"""Arhivo de implementación"""
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from infrastructure.models.user_model import UserModel

class UserRepositoryImpl(UserRepository):
    """Implementación de User Repository"""

    def create(self, user: User):
        model = UserModel.objects.create( # pylint: disable=no-member
            name=user.name,
            email=user.email,
            password_hash=user.password_hash
        )

        return User(
            id=model.id,
            name=model.name,
            email=model.email,
            password_hash=model.password_hash,
            created_at=model.created_at
        )

    def get_all(self):
        pass

    def get_by_id(self, user_id):
        pass

    def update(self, user_id):
        pass

    def dalete(self, user_id):
        pass
