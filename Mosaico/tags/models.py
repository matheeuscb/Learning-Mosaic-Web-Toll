#-*- coding: utf-8 -*-
from django.db import models


#class CursoManager(models.Manager):

	#def pesquisa(self, query):
		#return self.get_queryset().filter(
			#models.Q(name__icontains=query) | \
			#models.Q(description__icontains=query)
		#)

class Tag(models.Model):

	name = models.CharField('Nome', max_length=100)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now_add=True)

	#objects = CursoManager()

	def __str__(self):
		return self.name

	class Meta: 
		verbose_name = 'Tag' #modifica o nome na view
		verbose_name_plural = 'Tags'	
		ordering = ['name']