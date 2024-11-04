from django.db import models

# Create your models here.
# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    unidade = models.ForeignKey('Unidade', related_name='avisos', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.unidade}: {self.titulo} - {self.data}'
    
class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    professores = models.ManyToManyField('Professor', blank=True)  # Referencia o modelo Professor por string
    cursos = models.ManyToManyField('Curso', blank=True)  # Corrige o nome do campo

    def alterar_situacao_aluno(self, aluno, situacao):
        if situacao in ['ativo', 'trancado']:
            aluno.status = situacao
            aluno.save()
    
    def __str__(self):
        return f'Fatec {self.nome}'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao_anos = models.IntegerField()
    duracao_semestres = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, related_name='materias', on_delete=models.CASCADE)
    status_choices = [
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('reprovado', 'Reprovado'),
        ('nao_cursado', 'Não cursado'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default='nao_cursado')
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
class Aluno(AbstractUser):
    # ...
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='aluno_set',  # Define um nome específico para o Aluno
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='aluno',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='aluno_permissions',  # Define um nome específico para o Aluno
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='aluno',
    )
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
    def __str__(self):
        return self.username

class Professor(AbstractUser):
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='professor_set',  # Define um nome específico para o Professor
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='professor',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='professor_permissions',  # Define um nome específico para o Professor
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='professor',
    )
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
    
    def __str__(self):
        return self.username

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    nota = models.FloatField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, related_name='atividades', on_delete=models.CASCADE)

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE)
    frequencia = models.FloatField(default=0.0)
    
    class Meta:
        unique_together = ('aluno', 'materia')
        
    def __str__(self):
        return f'{self.aluno} - {self.materia}'
