from django.db import models
import uuid

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    # company
    city = models.CharField(blank=True, null=True,max_length=200)
    # tags =
    
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True,editable=False)

    
    def __str__(self) -> str:
        return self.title