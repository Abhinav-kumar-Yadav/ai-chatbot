from django.db import models


class Users(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Users"
