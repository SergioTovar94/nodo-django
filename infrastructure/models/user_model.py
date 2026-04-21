"""User Model"""
from django.db import models

class UserModel(models.Model):
    "Parseo a repo"
    name = models.CharField(max_length=100)
    email =  models.EmailField(unique=True, max_length=200)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Nombre de la tabla"""
        db_table = "users"
