from django.contrib import admin
from .models import Slider


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title','order']