from django.db.models import Model, CharField, IntegerField, BooleanField, ImageField, FileField, ForeignKey, OneToOneField, CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lead(Model):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    age = IntegerField(default=0)
    agent = ForeignKey('Agent', on_delete=CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(Model):
    user = OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return self.user.email



