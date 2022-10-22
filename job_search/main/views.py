from django.shortcuts import render
from .models import Vacancy


def vacancies_view(request):
    qs = Vacancy.objects.all()
    context = {'object_list': qs}
    return render(request, 'main/general.html', context)
