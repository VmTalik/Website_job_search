from django.contrib import admin
from .models import City, ProgrammingLanguage, Vacancy
from django.contrib.admin.models import LogEntry

admin.site.register([City, ProgrammingLanguage, Vacancy])

#Удаление последних действий в админ панеле
#LogEntry.objects.all().delete()