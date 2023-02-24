from django.urls import path
from vacancies import views

urlpatterns = [
    path('',views.vacancies, name='vacancies'),
    path('vacancy/<str:pk>', views.vacancy, name='vacancy')
]

