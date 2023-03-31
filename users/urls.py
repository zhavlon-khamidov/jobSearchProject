from django.urls import path
from users.views import logout_user, login_user, register_user

urlpatterns = [
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('register', register_user, name="registration"),
]