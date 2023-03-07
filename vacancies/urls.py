from django.urls import path
from vacancies import views

urlpatterns = [
    path('',views.vacancies, name='vacancies'),
    path('vacancy/<str:pk>', views.vacancy, name='vacancy'),
    path('create/',views.createVacancy, name='createVacancy'),
    path('update/<str:pk>',views.updateVacancy, name='updateVacancy'),
    path('delete/<str:pk>',views.deleteVacancy, name='deleteVacancy'),
]

