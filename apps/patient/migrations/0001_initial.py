# Generated by Django 4.2.1 on 2023-05-17 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Лечение')),
            ],
            options={
                'verbose_name': 'Лечение',
                'verbose_name_plural': 'Лечения',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='фио')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='пол')),
                ('age', models.CharField(blank=True, max_length=221, null=True, verbose_name='возраст')),
                ('simtom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Гастро -симптомы')),
                ('anketa', models.CharField(blank=True, max_length=255, null=True, verbose_name='Анкета')),
                ('rev_simtom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ревматологические симптомы')),
                ('start_date', models.CharField(blank=True, max_length=221, null=True, verbose_name='Поступил')),
                ('end_date', models.CharField(blank=True, max_length=221, null=True, verbose_name='выписка')),
                ('kd', models.CharField(blank=True, max_length=255, null=True, verbose_name='КД')),
                ('do_gos', models.CharField(blank=True, max_length=255, null=True, verbose_name='До госпитализации')),
                ('pao', models.CharField(blank=True, max_length=255, null=True, verbose_name='ПАО')),
                ('ivl', models.CharField(blank=True, max_length=255, null=True, verbose_name='ИВЛ')),
                ('isxod', models.CharField(blank=True, max_length=255, null=True, verbose_name='Исход')),
                ('dead', models.CharField(blank=True, max_length=255, null=True, verbose_name='Умер')),
                ('one_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='1 месяц')),
                ('two_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='2 месяц')),
                ('three_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='3 месяц')),
                ('four_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='4 месяц')),
                ('five_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='5 месяц')),
                ('six_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='6 месяц')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sxema', models.TextField(blank=True, null=True, verbose_name='Схема')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('lichenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='patient.licenie', verbose_name='Вариант')),
            ],
            options={
                'verbose_name': 'Вариант',
                'verbose_name_plural': 'Варианты',
            },
        ),
        migrations.CreateModel(
            name='Lechenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('licenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licenies', to='patient.licenie', verbose_name='Лечение')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lichenies', to='patient.patients', verbose_name='Пациент')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kt_1', models.FloatField(blank=True, default=0, null=True, verbose_name='КТ 1')),
                ('kt_2', models.FloatField(blank=True, default=0, null=True, verbose_name='КТ 2')),
                ('kt_3', models.FloatField(blank=True, default=0, null=True, verbose_name='КТ 3')),
                ('kt_4', models.FloatField(blank=True, default=0, null=True, verbose_name='КТ 4')),
                ('kt_5', models.FloatField(blank=True, default=0, null=True, verbose_name='КТ 5')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kt', to='patient.patients', verbose_name='Пациент')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Crp_Rbc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('crp', models.FloatField(default=0, verbose_name='CRP')),
                ('wbc', models.FloatField(default=0, verbose_name='RBC')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crp_rbc', to='patient.patients', verbose_name='Пациент')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Analiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('RBC_1', models.CharField(default=0, max_length=255, verbose_name='Количество эритроцитов на первые сутки')),
                ('RBC_2', models.CharField(default=0, max_length=255, verbose_name='Количество эритроцитов на вторые сутки')),
                ('RBC_3', models.CharField(default=0, max_length=255, verbose_name='Количество эритроцитов на третьи сутки')),
                ('wbc_1', models.CharField(default=0, max_length=255, verbose_name='Количество лейкоцитов на первые сутки')),
                ('wbc_2', models.CharField(default=0, max_length=255, verbose_name='Количество лейкоцитов на вторые сутки')),
                ('wbc_3', models.CharField(default=0, max_length=255, verbose_name='Количество лейкоцитов на третьи сутки')),
                ('plt_1', models.CharField(default=0, max_length=255, verbose_name='Количество тромбоцитов на первые сутки')),
                ('plt_2', models.CharField(default=0, max_length=255, verbose_name='Количество тромбоцитов на вторые сутки')),
                ('plt_3', models.CharField(default=0, max_length=255, verbose_name='Количество тромбоцитов на третьи сутки')),
                ('neu_1', models.CharField(default=0, max_length=255, verbose_name='Количество нейтрофилов на первые сутки')),
                ('neu_2', models.CharField(default=0, max_length=255, verbose_name='Количество нейтрофилов на вторые сутки')),
                ('neu_3', models.CharField(default=0, max_length=255, verbose_name='Количество нейтрофилов на третьи сутки')),
                ('lym_1', models.CharField(default=0, max_length=255, verbose_name='Количество лимфоцитов на первые сутки')),
                ('lym_2', models.CharField(default=0, max_length=255, verbose_name='Количество лимфоцитов на вторые сутки')),
                ('lym_3', models.CharField(default=0, max_length=255, verbose_name='Количество лимфоцитов на третьи сутки')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analiz', to='patient.patients', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Анализ',
                'verbose_name_plural': 'Анализы',
            },
        ),
    ]