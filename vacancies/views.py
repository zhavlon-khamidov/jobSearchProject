from django.shortcuts import render
from django.http import HttpResponse

def vacancies(request):
    return HttpResponse("List of all availabe vacancies")

def vacancy(request,id):
    return HttpResponse(f'Single vacancy with id: {id}')
