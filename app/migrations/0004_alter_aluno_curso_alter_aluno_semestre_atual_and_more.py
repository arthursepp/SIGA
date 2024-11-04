# Generated by Django 5.1.2 on 2024-11-04 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_aluno_semestre_atual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='app.curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='semestre_atual',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='unidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='app.unidade'),
        ),
    ]
