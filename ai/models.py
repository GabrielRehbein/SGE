from django.db import models


class AIResult(models.Model):
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Resultado da IA'
        verbose_name_plural = 'Resultados da IA'
