from django.urls import path

from .views import lichenie_detail, variant_detail, PatientCreate, PatientDetail, PatientList, analiz_detail, patient_detail

urlpatterns = [
    path("patients/", PatientList.as_view(), name="patient_list"),
    path("patients/create/", PatientCreate.as_view(), name="patient_create"),
    path("patients/<int:pk>/", patient_detail, name="patient_detail"),
    path("lichenie/<int:pk>/", lichenie_detail, name="lichenie_detail"),
    path("analiz/<int:pk>/", analiz_detail, name="analiz_detail"),
    path("variant/<int:pk>/", variant_detail, name="lichnie_detail"),



]
