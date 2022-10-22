from django.urls import path

from .views import vacancies_view

urlpatterns = [
    path('', vacancies_view),
    ]
