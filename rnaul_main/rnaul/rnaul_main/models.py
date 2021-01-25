from django.db import models

# Create your models here.

class Social(models.Model):
    social_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=500)

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=500)
    join_date = models.DateField()
    email = models.EmailField()
    
class Logins(models.Model):
    login_id = models.AutoField(primary_key=True)
    social_id = models.ForeignKey(Social, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    login_id = models.ForeignKey(Logins, on_delete=models.CASCADE)
    marked_data = models.CharField(max_length=2000)
    text_data = models.CharField(max_length=2000)
    date = models.DateField()

class Results(models.Model):
    result_id = models.AutoField(primary_key=True)
    data_id = models.ForeignKey(Data, on_delete=models.CASCADE)
    methrics = models.CharField(max_length=500)
    result = models.CharField(max_length=500)
