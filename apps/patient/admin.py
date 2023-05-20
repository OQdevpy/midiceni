from django.contrib import admin

from .models import KT, Analiz, Crp_Rbc, Licenie, Patients, Lechenie, Variant


@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ("id", "gender", "age", "simtom", "kd")


@admin.register(Analiz)
class AnalizAdmin(admin.ModelAdmin):
    pass


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


@admin.register(Licenie)
class LicenieAdmin(admin.ModelAdmin):
    inlines = [VariantInline]
admin.site.register(Lechenie)


admin.site.register(KT)
admin.site.register(Crp_Rbc)