from django.db import models
import datetime
from django.core.exceptions import ValidationError

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
        
        if semestres != anos * 2:
            raise ValidationError(
                f'A duração do curso deve ser de {anos} anos, ou seja, {anos * 2} semestres.'
            )
    
    def __str__(self):
        return f'{self.sigla} - {self.nome}'

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='materias_professor', blank=True, null=True)  # Ajuste do related_name
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='materias_curso', blank=True, null=True)  # Ajuste do related_name
    semestre = models.PositiveIntegerField(default=1)
    
    status_choices = [('ABERTA', 'Aberta'), ('FECHADA', 'Fechada')]
    status = models.CharField(max_length=7, choices=status_choices, default='ATIVA')
    
    def clean(self):
        if self.curso and self.semestre > self.curso.duracao_semestres:
            raise ValidationError(
                f'O curso "{self.curso}" possui apenas {self.curso.duracao_semestres} semestres.'
                f'Não é possível cadastrar uma matéria no {self.semestre}º semestre.'
            )
    
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
    
    status_choices = [('ATIVO', 'Ativo'), ('TRANCADO', 'Trancado'), ('FORMADO', 'Formado')]
    status = models.CharField(max_length=8, choices=status_choices, default='ATIVO')
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Desempenho(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='desempenho', blank=True, null=True)
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='desempenho', blank=True, null=True)
    presencas = models.IntegerField()
    notas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    
    status_choices = [
        ('APROVADO', 'Aprovado'),
        ('REPROVADO', 'Reprovado'),
        ('DISPENSADO', 'Dispensado'),
        ('EM ANDAMENTO', 'Em andamento')
    ]
    
    status = models.CharField(max_length=15, choices=status_choices, default='EM ANDAMENTO')
    
    class Meta:
        unique_together = ('aluno', 'materia')
        
    def definir_status(self):
        if self.materia.status == 'FECHADA' and self.notas is not None and self.notas >= 6.0:
            self.status = 'APROVADO'
            
        elif self.materia.status == 'FECHADA' and self.notas is not None and self.notas < 6.0:
            self.status = 'REPROVADO'
            
        elif self.materia.status == 'FECHADA' and self.presencas < 75:
            self.status = 'REPROVADO'
            
        elif self.materia.status == 'FECHADA' and self.presencas >= 75:
            self.status = 'APROVADO'
            
    def save(self, *args, **kwargs):
        self.definir_status()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.aluno} - {self.materia} - {self.data}'
