from django.contrib import admin
from .models import Nota

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "estado", "curso", "nota", "ano")
    list_filter = ("estado", "cidade", "curso", "ano")
    search_fields = ("nome", "cidade", "curso")
    ordering = ("-nota",)
