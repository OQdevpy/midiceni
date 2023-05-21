from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.patient.filterucn import toifa

from .forms import PatientFilterForm
from .models import KT, Analiz, Crp_Rbc, Lechenie, Licenie, Patients, Variant


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PatientList(ListView):
    model = Patients
    context_object_name = "patients"
    template_name = "patient_list.html"
    form_class = PatientFilterForm
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)

        if form.is_valid():
            filter_fields = [
                ("full_name__icontains", "full_name"),
                ("gender", "gender"),
                ("age", "age"),
                ("simtom", "simtom"),
                ("kd", "kd"),
                ("anketa", "anketa"),
                ("start_date__gte", "start_date"),
                ("end_date__lte", "end_date"),
                ("do_gos", "do_gos"),
                ("one_month", "one_month"),
                ("two_month", "two_month"),
                ("three_month", "three_month"),
                ("four_month", "four_month"),
                ("five_month", "five_month"),
                ("six_month", "six_month"),
                ("dead", "dead")
            ]

            for field, form_field_name in filter_fields:
                value = form.cleaned_data.get(form_field_name)
                if value:
                    queryset = queryset.filter(**{field: value})
        return queryset



class PatientCreate(CreateView):
    model = Patients
    fields = [
        "full_name",
        "age",
        "gender",
        "simtom",
        "kd",
        "anket",
        "start_date",
        "end_date",
        "do_gos",
    ]
    template_name = "patient_create.html"  # путь к шаблону
    success_url = reverse_lazy("patient_list")


class PatientDetail(DetailView):
    model = Patients
    template_name = "patient_detail.html"
    context_object_name = "object"

    def get_object(self, queryset=None):  # sourcery skip: avoid-builtin-shadow
        object = super().get_object(queryset=queryset)
        variants = Variant.objects.filter(patient_id__patient_id=self.kwargs['pk'])
        lichenie = Lechenie.objects.filter(patient_id=self.kwargs['pk'])
        
        if self.request.method == 'GET':
            if date := self.request.GET.get('date'):
                variants = variants.filter(created_at__date=date)
        
        object.lichenies.set(lichenie)
        # object.lichenies.variants = variants
        return object
    


def patient_detail(req,pk):

    patient = Patients.objects.get(id=pk)
    lichenie = Lechenie.objects.filter(patient_id=patient)
    variants = Variant.objects.filter(lichenie=lichenie.first().licenie)
    age = int(float(patient.age))
    gender = patient.gender

    
    
    

    

    if req.method == 'POST':
        selected_items = req.POST.getlist('selected_items')  # Get the selected checkbox values
        Variant.objects.filter(id__in=selected_items).delete() 
    
    if req.method == 'GET':
        if date := req.GET.get('date'):
            variants = variants.filter(created_at__date=date)
    variants_id = variants.values_list('id',flat=True)

        
    return render(req,'patient_detail.html',{'object':patient,'lichenies':lichenie,'variants':variants_id})
    

def analiz_detail(req,pk):
    patient = Patients.objects.get(id=pk)
    analiz = Analiz.objects.filter(patient=patient)

    return render(req,'analiz.html',{'analizs':analiz,'patient':patient})


def xolat(kt):

    if kt<=25:
        return 1
    elif  kt<=50:
        return 2
    elif kt<=75:
        return 3
    else:
        return 4




def lichenie_detail(req, pk):
    lichenie = Lechenie.objects.get(id=pk)
    patient = Patients.objects.get(id=lichenie.patient_id.id)
    kt = KT.objects.get(patient=patient)
    crp_rbc = Crp_Rbc.objects.get(patient=patient)
    

    return render(req,'lichenie.html',{'object':lichenie})



def variant_detail(req,pk):
    variant = Variant.objects.get(id=pk)

    return render(req,'variant.html',{'variant':variant})

