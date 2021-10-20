from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(db_column="accountId",primary_key=True)
    email = models.EmailField(db_column="email",max_length=100,unique=True)
    pwd = models.TextField(db_column="password",max_length=250)
    createdAt = models.DateTimeField(db_column="ac_createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField(db_column="ac_updatedAt",auto_now=True)

    def __str__(self):
        return "Account "+self.email