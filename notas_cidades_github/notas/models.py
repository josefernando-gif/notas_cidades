from django.db import models

class Nota(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100, db_index=True)
    estado = models.CharField(max_length=2, default="MT")
    curso = models.CharField(max_length=120, blank=True)
    nota = models.DecimalField(max_digits=7, decimal_places=2)
    ano = models.PositiveIntegerField(default=2026)

    class Meta:
        ordering = ["-nota", "nome"]
        indexes = [
            models.Index(fields=["cidade", "-nota"]),
            models.Index(fields=["ano", "-nota"]),
        ]

    def __str__(self):
        return f"{self.nome} - {self.nota}"
