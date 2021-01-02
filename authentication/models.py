from django.contrib import auth
from django.db import models


class User(auth.models.User):
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return "{} -{}".format(self.id, self.email)
