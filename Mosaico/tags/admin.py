from django.contrib import admin

from .models import Tag

class TagAdmin (admin.ModelAdmin):

	list_display = ['name', 'created_at']
	search_fields = ['name']

admin.site.register(Tag, TagAdmin)