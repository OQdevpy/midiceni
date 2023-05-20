from collections import Counter

from apps.patient.models import Analiz





eritrositlar = {
    "м":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[4.3,5.7],
        'age2':[4.2,5.6],
        'age3':[3.8,5.8],

    },
    "ж":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[3.8,5.1],
        'age2':[3.8,5.3],
        'age3':[3.8,5.2],
    }
}


leykositlar = {"м":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[4,11],
        'age2':[4,11],
        'age3':[3.5,9],

    },
    "ж":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[4,11],
        'age2':[4,11],
        'age3':[3.5,9],
    }}

trobositlar = {"м":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[150,400],
        'age2':[150,400],
        'age3':[150,400],
},
    "ж":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[150,400],
        'age2':[150,400],
        'age3':[150,400],
}}

netrofilov  = {"м":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[1.8,7.7],
        'age2':[1.8,6.6],
        'age3':[1.8,6.7],
},
    "ж":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[1.8,7.7],
        'age2':[1.8,6.6],
        'age3':[1.8,6.7],
}}



limfositlar = {"м":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[1.5,5.5],
        'age2':[1.4,5.5],
        'age3':[1.2,4.8],
},
    "ж":{
        'age':[[18,45],[45,65],[65,100]],
        'age1':[1.5,4],
        'age2':[1.4,4],
        'age3':[1.2,3.8],
}}





from django.core.management.base import BaseCommand
from django.apps import apps
from collections import Counter

class Command(BaseCommand):
    help = 'Ajratib berish toifalarni hisoblash'

    def handle(self, *args, **options):
        Analiz = apps.get_model('patient', 'Analiz')
        analizlar = Analiz.objects.all()

        for analiz in analizlar:
            toifa = ajratib_ber(analiz)
            self.stdout.write(f'Bemor {analiz.id} {toifa} toifasiga kiradi.')

def ajratib_ber(analysis):
    all_results = [getattr(analysis, field.name) for field in analysis._meta.get_fields() if field.name.startswith(('RBC', 'wbc', 'plt', 'neu', 'lym'))]
    counts = Counter(all_results)
    most_common_result = counts.most_common(1)[0][0]

    return most_common_result

