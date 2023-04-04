from django.apps import AppConfig
from  django.core.signals import request_finished
from django.db.models.signals import post_save

def printInfo(**kwargs):
    print(kwargs)
    print("data saved")

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        post_save.connect(printInfo)
