from django.contrib import admin
from .models import Semestre, Matiere, Note

admin.site.register(Semestre)
admin.site.register(Matiere)
admin.site.register(Note)