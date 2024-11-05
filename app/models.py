from django.db import models
import datetime

class Unidade(models.Model):
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    cursos = models.ManyToManyField('Curso', related_name='unidades_curso', blank=True)  # Ajuste do related_name
    
    def __str__(self):
        return f'Fatec {self.cidade}'

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField(default=datetime.date.today)
    unidade = models.ForeignKey('Unidade', on_delete=models.CASCADE, related_name='avisos', blank=True, null=True)
    
    def __str__(self):
        return f'{self.unidade} - {self.titulo} - {self.data}'

class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=150)
    periodo_choices = [('MANHA', 'Manhã'), ('TARDE', 'Tarde'), ('NOITE', 'Noite')]
    periodo = models.CharField(max_length=5, choices=periodo_choices)
    duracao_anos = models.PositiveIntegerField()
    duracao_semestres = models.PositiveIntegerField()
    materias = models.ManyToManyField('Materia', related_name='cursos_materia', blank=True)  # Ajuste do related_name
    
    def validar_duracao(self):
        semestres = self.duracao_semestres
        anos = self.duracao_anos
        return semestres <= (anos * 2)
    
    def __str__(self):
        return f'{self.sigla} - {self.nome}'

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='materias_professor', blank=True, null=True)  # Ajuste do related_name
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='materias_curso', blank=True, null=True)  # Ajuste do related_name
    
    def __str__ (self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    matricula = models.CharField(max_length=13)
    email = models.EmailField()
    curso = models.ManyToManyField('Curso', related_name='professores_curso', blank=True)  # Ajuste do related_name
    materia = models.ManyToManyField('Materia', related_name='professores_materia', blank=True)  # Ajuste do related_name
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    matricula = models.CharField(max_length=13)
    email = models.EmailField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='alunos_curso', blank=True, null=True)  # Ajuste do related_name
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
