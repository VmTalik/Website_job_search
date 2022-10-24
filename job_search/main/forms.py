from django import forms

from main.models import City, ProgrammingLanguage


class VacancyFindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name="slug",
                                  required=False, widget=forms.Select(attrs={"class": "form-control"}),
                                  label='Город')
    language = forms.ModelChoiceField(queryset=ProgrammingLanguage.objects.all(), to_field_name="slug",
                                      required=False, widget=forms.Select(attrs={"class": "form-control"}),
                                      label='Язык программирования')
