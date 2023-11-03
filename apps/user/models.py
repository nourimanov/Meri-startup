from django.db import models


class UserModel(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=300, )


class Meta:
    app_label = 'user'


class SignIn(models.Model):
    phone = models.IntegerField()
    password = models.CharField(max_length=300)


