
from django.db import models

class Film(models.Model):
    title = models.CharField("Название фильма", max_length=100)
    short_description = models.CharField('Краткое описание фильма', max_length=200)
    review = models.TextField("Рецензия", max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

# Create your models here.


# Create your models here.
