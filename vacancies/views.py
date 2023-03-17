from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from . import models
from .forms import VacancyForm

data = [
    {'id':1, 'name':'Abai','surname': 'Tentimishov'},
    {'id':2, 'name':'Azman','surname': 'Muratbekov'},
    {'id':3, 'name':'Aktan','surname': 'Temirkanov'},
    {'id':4, 'name':'Nurislam','surname': 'Orozbaev'},
    {'id':5, 'name':'Sultan','surname': 'Sabatbekov'},
]


def deleteVacancy(request,pk):
    vacancy = models.Vacancy.objects.get(id=pk)
    
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancies')
    
    context = {'vacancy': vacancy}
    return render(request, 'delete.html', context)

def createVacancy(request):
    form = VacancyForm()
    
    if request.method == "POST":
        form = VacancyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vacancies')
    context = {'form': form}
    return render(request, 'vacancy-form.html',context)

def updateVacancy(request, pk):
    vacancy = models.Vacancy.objects.get(id=pk)
    form = VacancyForm(instance=vacancy)
    
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy', vacancy.id)
    context = {'form': form}
    return render(request, 'vacancy-form.html',context)

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
