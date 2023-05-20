from apps.patient.models import Analiz


age = [[18,45],[46,64],[65,100]]

eritrositlar = {
    "м":{
       
        'age1':[4.3,5.7],
        'age2':[4.2,5.6],
        'age3':[3.8,5.8],

    },
    "ж":{
       
        'age1':[3.8,5.1],
        'age2':[3.8,5.3],
        'age3':[3.8,5.2],
    }
}


leykositlar = {"м":{
       
        'age1':[4,11],
        'age2':[4,11],
        'age3':[3.5,9],

    },
    "ж":{
       
        'age1':[4,11],
        'age2':[4,11],
        'age3':[3.5,9],
    }}

trobositlar = {"м":{
       
        'age1':[150,400],
        'age2':[150,400],
        'age3':[150,400],
},
    "ж":{
       
        'age1':[150,400],
        'age2':[150,400],
        'age3':[150,400],
}}

netrofilov  = {"м":{
       
        'age1':[1.8,7.7],
        'age2':[1.8,6.6],
        'age3':[1.8,6.7],
},
    "ж":{
       
        'age1':[1.8,7.7],
        'age2':[1.8,6.6],
        'age3':[1.8,6.7],
}}



limfositlar = {"м":{
       
        'age1':[1.5,5.5],
        'age2':[1.4,5.5],
        'age3':[1.2,4.8],
},
    "ж":{
       
        'age1':[1.5,4],
        'age2':[1.4,4],
        'age3':[1.2,3.8],
}}



def toifa(gender,age_,analiz_id):  # sourcery skip: low-code-quality, remove-redundant-if
    analiz = Analiz.objects.get(id=analiz_id)
    field_names = [field.name for field in analiz._meta.fields]
    field_values = []

    # Retrieve field values, considering blank=True and null=True
    for field_name in field_names:
        field_value = getattr(analiz, field_name)
        if field_value is not None and field_value != "":
            field_values.append(field_value)
        else:
            field_values.append(0)

    

    ind = 0
    for j,i in enumerate(age,start=1):

        if age_>= i[0] and age_<= i[1]:
            ind = j
    xolat  = []
    field_values = list(map(float,field_values[4:]))

    leykos = leykositlar[gender][f'age{ind}']
    eritros = eritrositlar[gender][f'age{ind}']
    trobos = trobositlar[gender][f'age{ind}']
    netros = netrofilov[gender][f'age{ind}']
    limfos = limfositlar[gender][f'age{ind}']
    xolat1 = list(
        map(lambda x: x >= eritros[0] and x <= eritros[1], field_values[:3])
    )
    xolat2 = list(
        map(lambda x: x >= leykos[0] and x <= leykos[1], field_values[3:6])
    )
    xolat3 = list(
        map(lambda x: x >= trobos[0] and x <= trobos[1], field_values[6:9])
    )
    xolat4 = list(
        map(lambda x: x >= netros[0] and x <= netros[1], field_values[9:12])
    )
    xolat5 = list(
        map(lambda x: x >= limfos[0] and x <= limfos[1], field_values[12:15])
    )
    return {
        "eritrositlar": xolat1,
        "leykositlar": xolat2,
        "trobositlar": xolat3,
        "netrofilov": xolat4,
        "limfositlar": xolat5,
    }






        
   