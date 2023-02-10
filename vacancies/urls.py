from django.urls import path
from vacancies import views

urlpatterns = [
    path('',views.vacancies, name='vacancies'),
    path('vacancy/<int:id>', views.vacancy, name='vacancy')
]

