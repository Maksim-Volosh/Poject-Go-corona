from django.db import models
from django.urls import reverse

class ModelForm(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone_number = models.CharField(max_length=255, verbose_name="Номер телефона")
    city = models.CharField(max_length=255, verbose_name="Город")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"