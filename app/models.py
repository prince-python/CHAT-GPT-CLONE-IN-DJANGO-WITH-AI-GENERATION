from django.db import models

class User(models.Model):
    name=models.CharField(max_length=400)
    email= models.EmailField( max_length=254)
    pwd=models.CharField(max_length=250)
    
class qna(models.Model):
    que=models.TextField()
    ans=models.TextField()