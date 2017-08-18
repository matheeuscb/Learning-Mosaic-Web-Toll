from django.contrib import admin

from .models import Curso

class CursoAdmin (admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name','slug']

admin.site.register(Curso, CursoAdmin)