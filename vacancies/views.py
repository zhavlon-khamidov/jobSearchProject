from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
    return render(request,'vacancies.html',
                  {'page':"Vacancies",'students':data})

def vacancy(request,id):
    # return HttpResponse(f'Single vacancy with id: {id}')
    student = None
    for s in data:
        if s['id'] == id:
            student = s
            break
    return render(request, 'single-vacancy.html',
                  {'page':'Single-vacancy','student':student})
