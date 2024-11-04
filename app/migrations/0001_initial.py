# Generated by Django 5.1.2 on 2024-11-04 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao_anos', models.IntegerField()),
                ('duracao_semestres', models.IntegerField()),
                ('periodo', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('semestre', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('materias', models.ManyToManyField(blank=True, related_name='professores_materias', to='app.materia')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materias_professor', to='app.professor'),
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('cursos', models.ManyToManyField(blank=True, related_name='unidades', to='app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretarios', to='app.unidade')),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores', to='app.unidade'),
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avisos', to='app.unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('semestre_atual', models.IntegerField()),
                ('media_final', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('ATIVO', 'Ativo'), ('TRANCADO', 'Trancado'), ('FORMADO', 'Formado')], default='ATIVO', max_length=8)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='app.curso')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='app.unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequencia', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('em_andamento', 'Em Andamento'), ('concluido', 'Concluído'), ('reprovado', 'Reprovado'), ('nao_cursado', 'Não cursado')], default='nao_cursado', max_length=15)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='app.aluno')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='app.materia')),
            ],
            options={
                'unique_together': {('aluno', 'materia')},
            },
        ),
    ]
