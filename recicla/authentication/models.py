from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, name, password=None):
        if not name:
            raise ValueError("O campo nome é obrigatório.")
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, password):
        user = self.create_user(name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
