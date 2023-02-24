from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models

data = [
    {'id':1, 'name':'Abai','surname': 'Tentimishov'},
    {'id':2, 'name':'Azman','surname': 'Muratbekov'},
    {'id':3, 'name':'Aktan','surname': 'Temirkanov'},
    {'id':4, 'name':'Nurislam','surname': 'Orozbaev'},
    {'id':5, 'name':'Sultan','surname': 'Sabatbekov'},
]

def vacancies(request):
    # html_text = loader.render_to_string('vacancies.html')
    # return HttpResponse(html_text)
    data = models.Vacancy.objects.all()
    return render(request,'vacancies.html',
                  {'page':"Vacancies",'vacancies':data})

def vacancy(request,pk):
    # return HttpResponse(f'Single vacancy with id: {id}')
    vacancy = models.Vacancy.objects.get(id=pk)
    """ for s in data:
        if s['id'] == id:
            student = s
            break """
    return render(request, 'single-vacancy.html',
                  {'page':'Single-vacancy','vacancy':vacancy})
