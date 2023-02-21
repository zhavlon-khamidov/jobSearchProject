from django.db import models
import uuid

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    company = models.ForeignKey('Company',null=True,on_delete = models.CASCADE, default=None)
    city = models.CharField(blank=True, null=True,max_length=200)
    tags = models.ManyToManyField('Tag')
    
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)

    
    def __str__(self) -> str:
        return self.title + ' (' + str(self.company) + ')'
    

class Company(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=25, blank=True,null=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=255, blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    