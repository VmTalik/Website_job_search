from django.shortcuts import render

from .forms import VacancyFindForm
from .models import Vacancy


def vacancies_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        d_choice = {}
        if city:
            d_choice['city__slug'] = city
        if language:
            d_choice['language__slug'] = language
        qs = Vacancy.objects.filter(**d_choice)
    form = VacancyFindForm
    context = {'object_list': qs, 'form': form}
    return render(request, 'main/general.html', context)
