from django.contrib import admin
from . import models

admin.site.register(models.Vacancy)
admin.site.register(models.Company)
admin.site.register(models.Tag)

