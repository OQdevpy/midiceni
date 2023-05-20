from django import forms
from django.forms import DateInput


class PatientFilterForm(forms.Form):
    full_name = forms.CharField(required=False, label="ФИО")
    gender = forms.CharField(required=False, label="Пол")
    age = forms.IntegerField(required=False, label="Вес")
    simtom = forms.CharField(required=False, label="Симтом")
    kd = forms.CharField(required=False, label="КД")

    anketa = forms.CharField(required=False, label="Анкета")
    start_date = forms.DateField(required=False, label="Дата поступления", widget=DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, label="Дата окончания поступления",
                               widget=DateInput(attrs={'type': 'date'}))

    anket = forms.CharField(required=False, label="Анкета")
    start_date = forms.DateField(required=False, label="Дата поступления", widget=DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(
        required=False, label="Дата окончания поступления", widget=DateInput(attrs={"type": "date"})
    )

    do_gos = forms.CharField(required=False, label="До госпитализации")
    one_month = forms.CharField(required=False, label="За месяц")
    two_month = forms.CharField(required=False, label="За два месяца")
    three_month = forms.CharField(required=False, label="За три месяца")
    four_month = forms.CharField(required=False, label="За четыре месяца")
    five_month = forms.CharField(required=False, label="За пять месяца")
    six_month = forms.CharField(required=False, label="За шесть месяца")
    dead = forms.CharField(required=False, label="Умер")
