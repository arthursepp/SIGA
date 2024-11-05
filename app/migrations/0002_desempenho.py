# Generated by Django 5.1.2 on 2024-11-05 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desempenho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presencas', models.IntegerField()),
                ('notas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('data', models.DateField(auto_now_add=True)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desempenho', to='app.aluno')),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desempenho', to='app.materia')),
            ],
            options={
                'unique_together': {('aluno', 'materia')},
            },
        ),
    ]