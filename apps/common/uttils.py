import xlrd
from russian_names import RussianNames

from apps.patient.models import KT, Analiz, Crp_Rbc, Patients


def import_data(file_path):
    # print("Importing data from {} file".format(file_path))
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_index(0)
    # print(worksheet.nrows)
    for row_idx in range(1, worksheet.nrows):
        full_name = worksheet.cell(row_idx, 0).value
        gender = worksheet.cell(row_idx, 1).value
        age = worksheet.cell(row_idx, 2).value
        simtom = worksheet.cell(row_idx, 4).value
        anketa = worksheet.cell(row_idx, 3).value
        rev_simtom = worksheet.cell(row_idx, 5).value
        start_date = worksheet.cell(row_idx, 6).value
        # print(start_date)
        end_date = worksheet.cell(row_idx, 7).value
        kd = worksheet.cell(row_idx, 8).value
        do_gos = worksheet.cell(row_idx, 9).value
        pao = worksheet.cell(row_idx, 10).value
        ivl = worksheet.cell(row_idx, 11).value
        isxod = worksheet.cell(row_idx, 13).value
        one_month = worksheet.cell(row_idx, 14).value
        two_month = worksheet.cell(row_idx, 15).value
        three_month = worksheet.cell(row_idx, 16).value
        four_month = worksheet.cell(row_idx, 17).value
        five_month = worksheet.cell(row_idx, 18).value
        six_month = worksheet.cell(row_idx, 18).value
        dead = worksheet.cell(row_idx, 19).value
        Patients.objects.get_or_create(
            gender=gender,
            age=age,
            simtom=simtom,
            anketa=anketa,
            rev_simtom=rev_simtom,
            start_date=start_date,
            end_date=end_date,
            kd=kd,
            do_gos=do_gos,
            pao=pao,
            ivl=ivl,
            isxod=isxod,
            one_month=one_month,
            two_month=two_month,
            three_month=three_month,
            four_month=four_month,
            five_month=five_month,
            six_month=six_month,
            dead=dead,
        )




def import_data2(file_path):
    # print("Importing data from {} file".format(file_path))
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_index(0)
    for row_idx in range(1, worksheet.nrows):
        RBC_1 = worksheet.cell(row_idx, 0).value
        RBC_2 = worksheet.cell(row_idx, 1).value
        RBC_3 = worksheet.cell(row_idx, 2).value
        wbc_1 = worksheet.cell(row_idx, 3).value
        wbc_2 = worksheet.cell(row_idx, 4).value
        wbc_3 = worksheet.cell(row_idx, 5).value
        plt_1 = worksheet.cell(row_idx, 6).value
        plt_2 = worksheet.cell(row_idx, 7).value
        plt_3 = worksheet.cell(row_idx, 8).value
        neu_1 = worksheet.cell(row_idx, 9).value
        neu_2 = worksheet.cell(row_idx, 10).value
        neu_3 = worksheet.cell(row_idx, 11).value
        lym_1 = worksheet.cell(row_idx, 12).value
        lym_2 = worksheet.cell(row_idx, 13).value
        lym_3 = worksheet.cell(row_idx, 14).value
        # print(row_idx)
        patient = Patients.objects.get(id=row_idx)
        Analiz.objects.get_or_create(
            patient=patient,
            RBC_1=RBC_1,
            RBC_2=RBC_2,
            RBC_3=RBC_3,
            wbc_1=wbc_1,
            wbc_2=wbc_2,
            wbc_3=wbc_3,
            plt_1=plt_1,
            plt_2=plt_2,
            plt_3=plt_3,
            neu_1=neu_1,
            neu_2=neu_2,
            neu_3=neu_3,
            lym_1=lym_1,
            lym_2=lym_2,
            lym_3=lym_3,
        )


import xlrd

def import_data3(filepath):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_index(0)  # Specify the index of the sheet you want to work with
    
    for row_idx in range(1, worksheet.nrows):
        # print(worksheet.cell_value(row_idx, 1), worksheet.cell_value(row_idx, 2))
        kt_1 = worksheet.cell_value(row_idx, 1) if worksheet.cell_value(row_idx, 1) else 0 
        kt_2 = worksheet.cell_value(row_idx, 2) if worksheet.cell_value(row_idx, 2) else 0

        patient = Patients.objects.get(id=row_idx)  # Assuming 'Patients' is the correct model
        KT.objects.get_or_create(
            patient=patient,
            kt_1=kt_1,
            kt_2=kt_2,  
        )

def import_data4(filepath):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_index(0)  # Specify the index of the sheet you want to work with
    
    for row_idx in range(29, worksheet.nrows):
        crp = float(worksheet.cell_value(row_idx, 0)) if worksheet.cell_value(row_idx, 0) else 0 
        wbc = float(worksheet.cell_value(row_idx, 1)) if worksheet.cell_value(row_idx, 1) else 0
        patient = Patients.objects.get(id=row_idx)  
        # print([crp,wbc])# Assuming 'Patients' is the correct model
        Crp_Rbc.objects.get_or_create(
            patient=patient,
            crp=crp,
            wbc=wbc,  
        )



# wbcdef create_names_patients():
#
# # a=RussianNames(gender=0).get_person()
#
