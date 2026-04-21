from rest_framework.views import APIView
from rest_framework.response import Response


from application.use_cases.create_user import CreateUser
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl

class UserView(APIView):
    """Controlador"""
    def post(self, request):
        """Crear Usuario"""
        use_case = CreateUser(UserRepositoryImpl())

        user = use_case.execute(
            name = request.data["name"],
            email = request.data["email"],
            password_hash= request.data["password_hash"]
        )

        return Response({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
