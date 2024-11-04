from django.contrib.auth.models import User
from django.db import models

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    unidade = models.ForeignKey('Unidade', related_name='avisos', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.unidade}: {self.titulo} - {self.data}'
    
class Unidade(models.Model):    
    cidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)    
    cursos = models.ManyToManyField('Curso', blank=True, related_name='unidades')
    
    def __str__(self):
        return f'Fatec {self.cidade}'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao_anos = models.IntegerField()
    duracao_semestres = models.IntegerField()
    periodo_choices = [('manha', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')]
    periodo = models.CharField(choices=periodo_choices, max_length=10)
    
    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, related_name='materias', on_delete=models.CASCADE)
    semestre = models.IntegerField()    
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='materias_professor')
    
    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='alunos', blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alunos', blank=True, null=True)
    semestre_atual = models.IntegerField(blank=True, null=True)
    media_final = models.FloatField(default=0.0)
    status_choices = [('ATIVO', 'Ativo'), ('TRANCADO', 'Trancado'), ('FORMADO', 'Formado')]
    status = models.CharField(max_length=8, choices=status_choices, default='ATIVO')
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Professor(models.Model):   
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='professores')
    materias = models.ManyToManyField('Materia', blank=True, related_name='professores_materias')
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Secretaria(models.Model):    
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='secretarios')
        
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='matriculas')
    frequencia = models.FloatField(default=0.0)
    status_choices = [
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('reprovado', 'Reprovado'),
        ('nao_cursado', 'Não cursado'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default='nao_cursado')
    
    class Meta:
        unique_together = ('aluno', 'materia')
        
    def __str__(self):
        return f'{self.aluno} - {self.materia}'