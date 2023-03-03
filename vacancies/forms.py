from django.forms import ModelForm
from .models import Vacancy

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title','description','min_price','max_price','city','tags']