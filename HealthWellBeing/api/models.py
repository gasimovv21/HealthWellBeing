from django.db import models

class TextMessage(models.Model):
    text = models.CharField(
        'text',
        max_length=256
    )

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        ordering = ('text',)