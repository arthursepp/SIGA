from django.db import models
from django.contrib.auth.models import User  # Para associar professores e alunos
from django.core.validators import MinValueValidator, MaxValueValidator

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    aviso = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    semestre = models.PositiveIntegerField()
    periodo = models.CharField(
        max_length=10, choices=[('manhã', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')]
    )

    def __str__(self):
        return f"{self.nome} - {self.periodo} ({self.semestre}º Semestre)"

class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    materias = models.ManyToManyField('Materia', related_name='professores', blank=True)

    def __str__(self):
        return self.usuario.get_full_name()

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"

class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.usuario.get_full_name()

class MatriculaMateria(models.Model):
    STATUS_CHOICES = [
        ('EM ANDAMENTO', 'Em Andamento'),
        ('REPROVADO_POR_NOTA', 'Reprovado por Nota'),
        ('REPROVADO_POR_FALTA', 'Reprovado por Falta'),
        ('APROVADO', 'Aprovado'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    presenca = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EM ANDAMENTO')

    class Meta:
        unique_together = ('aluno', 'materia')

    def verificar_status(self):
        """Define o status do aluno com base na média e na presença."""
        if self.status == 'EM ANDAMENTO':
            return
        
        media = self.calcular_media()
        
        if self.presenca < 50:
            self.status = 'REPROVADO_POR_FALTA'
        elif media < 6:
            self.status = 'REPROVADO_POR_NOTA'
        else:
            self.status = 'EM ANDAMENTO'
            
        self.save()
        
    def calcular_media(self):
        """Calcula a média das atividades do aluno."""
        atividades = self.atividade_set.all()
        if atividades:
            return sum([atividade.nota for atividade in atividades]) / len(atividades)
        return 0

    def __str__(self):
        return f"{self.aluno} - {self.materia} ({self.status})"

class Atividade(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.materia.nome}"

class Nota(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        unique_together = ('atividade', 'aluno')

    def __str__(self):
        return f"{self.aluno} - {self.atividade} : {self.nota}"
