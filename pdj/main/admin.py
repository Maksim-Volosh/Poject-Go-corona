from django.contrib import admin
from .models import ModelForm  # Импортируйте вашу модель

class ModelFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'city', 'time_create', 'time_update')  # Определите отображаемые поля в списке

# Зарегистрируйте вашу модель с соответствующим административным классом
admin.site.register(ModelForm, ModelFormAdmin)
