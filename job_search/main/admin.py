from django.contrib import admin
from .models import City, ProgrammingLanguage

admin.site.register([City, ProgrammingLanguage])
