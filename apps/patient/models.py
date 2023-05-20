from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# import Sum
from django.db.models import Sum

from apps.common.models import BaseModel


class Patients(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name="фио", blank=True, null=True)
    gender = models.CharField(max_length=255, verbose_name="пол", blank=True, null=True)
    age = models.CharField(max_length=221,verbose_name="возраст", blank=True, null=True)
    simtom = models.CharField(max_length=255, verbose_name="Гастро -симптомы", blank=True, null=True)
    anketa = models.CharField(max_length=255, verbose_name="Анкета", blank=True, null=True)
    rev_simtom = models.CharField(max_length=255, verbose_name="Ревматологические симптомы", blank=True, null=True)
    start_date = models.CharField(max_length=221,verbose_name="Поступил", blank=True, null=True)
    end_date = models.CharField(max_length=221,verbose_name="выписка", blank=True, null=True)
    kd = models.CharField(max_length=255, verbose_name="КД", blank=True, null=True)
    do_gos = models.CharField(max_length=255, verbose_name="До госпитализации", blank=True, null=True)
    pao = models.CharField(max_length=255, verbose_name="ПАО", blank=True, null=True)
    ivl = models.CharField(max_length=255, verbose_name="ИВЛ", blank=True, null=True)
    isxod = models.CharField(max_length=255, verbose_name="Исход", blank=True, null=True)
    dead = models.CharField(max_length=255, verbose_name="Умер", blank=True, null=True)
    one_month = models.CharField(max_length=255, verbose_name="1 месяц", blank=True, null=True)
    two_month = models.CharField(max_length=255, verbose_name="2 месяц", blank=True, null=True)
    three_month = models.CharField(max_length=255, verbose_name="3 месяц", blank=True, null=True)
    four_month = models.CharField(max_length=255, verbose_name="4 месяц", blank=True, null=True)
    five_month = models.CharField(max_length=255, verbose_name="5 месяц", blank=True, null=True)
    six_month = models.CharField(max_length=255, verbose_name="6 месяц", blank=True, null=True)

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return str(self.id)


class Analiz(BaseModel):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name="Пациент",related_name="analiz")
    RBC_1 = models.CharField(
        max_length=255, verbose_name="Количество эритроцитов на первые сутки", default = 0
    )
    RBC_2 = models.CharField(
        max_length=255, verbose_name="Количество эритроцитов на вторые сутки", default = 0
    )
    RBC_3 = models.CharField(
        max_length=255, verbose_name="Количество эритроцитов на третьи сутки", default = 0
    )
    wbc_1 = models.CharField(
        max_length=255, verbose_name="Количество лейкоцитов на первые сутки", default = 0
    )
    wbc_2 = models.CharField(
        max_length=255, verbose_name="Количество лейкоцитов на вторые сутки", default = 0
    )
    wbc_3 = models.CharField(
        max_length=255, verbose_name="Количество лейкоцитов на третьи сутки", default = 0
    )
    plt_1 = models.CharField(
        max_length=255, verbose_name="Количество тромбоцитов на первые сутки", default = 0
    )
    plt_2 = models.CharField(
        max_length=255, verbose_name="Количество тромбоцитов на вторые сутки", default = 0
    )
    plt_3 = models.CharField(
        max_length=255, verbose_name="Количество тромбоцитов на третьи сутки", default = 0
    )
    neu_1 = models.CharField(
        max_length=255, verbose_name="Количество нейтрофилов на первые сутки", default = 0
    )
    neu_2 = models.CharField(
        max_length=255, verbose_name="Количество нейтрофилов на вторые сутки", default = 0
    )
    neu_3 = models.CharField(
        max_length=255, verbose_name="Количество нейтрофилов на третьи сутки", default = 0
    )
    lym_1 = models.CharField(
        max_length=255, verbose_name="Количество лимфоцитов на первые сутки", default = 0
    )
    lym_2 = models.CharField(
        max_length=255, verbose_name="Количество лимфоцитов на вторые сутки", default = 0
    )
    lym_3 = models.CharField(
        max_length=255, verbose_name="Количество лимфоцитов на третьи сутки", default = 0
    )

    class Meta:
        verbose_name = "Анализ"
        verbose_name_plural = "Анализы"

class Licenie(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Лечение", blank=True, null=True)
    


    class Meta:
        verbose_name = "Лечение"
        verbose_name_plural = "Лечения"


    def __str__(self):
        return self.name



class Lechenie(BaseModel):
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name="Пациент",related_name="lichenies")
    licenie = models.ForeignKey(Licenie ,on_delete=models.CASCADE, verbose_name="Лечение",related_name="licenies")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    @property
    def get_all_variants_price(self):
        return self.licenie.variants.all().aggregate(Sum("price"))["price__sum"]



class Variant(BaseModel):
    lichenie = models.ForeignKey(Licenie, on_delete=models.CASCADE, verbose_name="Вариант",related_name="variants")
    sxema = models.TextField(verbose_name="Схема", blank=True, null=True)
    price = models.DecimalField(  max_digits=10, decimal_places=2, verbose_name="Цена",default=0)
    # mediakament = models.CharField(max_length=255, verbose_name="Медикамент", blank=True, null=True)
    # ed_iz = models.CharField(max_length=255, verbose_name="Ед.изм", blank=True, null=True)
    # periodnichnost = models.CharField(max_length=255, verbose_name="Периодичность", blank=True, null=True)
    # doza_naznach = models.CharField(max_length=255, verbose_name="Доза назначенная", blank=True, null=True)
    # kolvo_procedur = models.CharField(max_length=255, verbose_name="Количество процедур", blank=True, null=True)
    # sposob_ispolneniya = models.CharField(max_length=255, verbose_name="Способ исполнения", blank=True, null=True)
    # price = models.CharField(max_length=255, verbose_name="Цена", blank=True, null=True)
    # analiz = models.ForeignKey(Analiz, on_delete=models.CASCADE, verbose_name="Анализ", blank=True, null=True)



    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"


    def __str__(self):
        return self.lichenie.name


# class Variants(BaseModel):
#     patient_id = models.ForeignKey(Lechenie, on_delete=models.CASCADE, verbose_name="Вариант",related_name="variants")
#     lechenie = models.CharField(max_length=255, verbose_name="Лечение", blank=True, null=True)
#     mediakament = models.CharField(max_length=255, verbose_name="Медикамент", blank=True, null=True)
#     ed_iz = models.CharField(max_length=255, verbose_name="Ед.изм", blank=True, null=True)
#     periodnichnost = models.CharField(max_length=255, verbose_name="Периодичность", blank=True, null=True)
#     doza_naznach = models.CharField(max_length=255, verbose_name="Доза назначенная", blank=True, null=True)
#     kolvo_procedur = models.CharField(max_length=255, verbose_name="Количество процедур", blank=True, null=True)
#     sposob_ispolneniya = models.CharField(max_length=255, verbose_name="Способ исполнения", blank=True, null=True)
#     price = models.CharField(max_length=255, verbose_name="Цена", blank=True, null=True)
#     analiz = models.ForeignKey(Analiz, on_delete=models.CASCADE, verbose_name="Анализ", blank=True, null=True)



#     class Meta:
#         verbose_name = "Вариант"
#         verbose_name_plural = "Варианты"


#     def __str__(self):
#         return self.lechenie



class KT(BaseModel):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name="Пациент",related_name="kt")
    kt_1 =models.FloatField(verbose_name="КТ 1", default=0,blank=True, null=True)
    kt_2 =models.FloatField(verbose_name="КТ 2", default=0,blank=True, null=True)
    kt_3 =models.FloatField(verbose_name="КТ 3", default=0,blank=True, null=True)
    kt_4 =models.FloatField(verbose_name="КТ 4", default=0,blank=True, null=True)
    kt_5 =models.FloatField(verbose_name="КТ 5", default=0,blank=True, null=True)


    def xolat(self,kt):

        if kt<=25:
            return 1
        elif  kt<=50:
            return 2
        elif kt<=75:
            return 3
        else:
            return 4

    def __str__(self):
        return str(self.id)
    

    def save(self,*args, **kwargs):
    
        lechenie,created = Lechenie.objects.get_or_create(patient_id=self.patient,licenie_id=self.xolat(self.kt_1))
        lechenie.save()
        super(KT, self).save(*args, **kwargs)
    

    

    

class Crp_Rbc(BaseModel):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name="Пациент",related_name="crp_rbc")
    crp = models.FloatField(verbose_name="CRP", default=0)
    wbc = models.FloatField(verbose_name="RBC", default=0)

    def __str__(self):
        return str(self.id)