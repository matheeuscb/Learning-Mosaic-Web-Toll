#-*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class Usuario(AbstractBaseUser,PermissionsMixin):

	name = models.CharField('nome', max_length=30)
	lastname = models.CharField('sobrenome', max_length=50)
	email = models.EmailField('email', unique=True)
	imagem = models.ImageField(upload_to='perfil/', blank=True, null=True)

	

	USERNAME_FIELD = 'email'

	objects=UserManager()


class Canvas(models.Model):
	
	nome_canvas = models.CharField('nome_canvas', max_length=45)
	descricao_canvas = models.TextField('Descrição', blank=True)
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	objects=models.Manager()

class Areas(models.Model):
	nome_area = models.CharField('Nome Area', max_length=30)
	dicas_area = models.TextField('Dicas Area', blank=True)
	id_canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE)
	objects=models.Manager()


class Mosaico(models.Model):
	id_canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE)
	id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

 	objects=models.Manager()


class Nivel(models.Model):
	tipo_nivel = models.CharField('Tipo Nivel', max_length=10)


class Verbo(models.Model):
 	nome_verbo = models.CharField('Nome Verbo', max_length=10)
 	id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

class Status(models.Model):
	nome_status = models.CharField('Status', max_length=20)
	cor_status = models.CharField('Cor', max_length=20)

class Objetivos_De_Aprendizagem(models.Model):
	descricao_objetivos = models.TextField('Descrição', blank=True)
	status_inicial = models.ForeignKey(Status, related_name='status_inicial', on_delete=models.SET_NULL, null=True) 
	status_final = models.ForeignKey(Status, related_name='status_final', on_delete=models.SET_NULL, null=True)
	id_mosaico = models.ForeignKey(Mosaico, on_delete=models.CASCADE)
	id_verbo = models.ForeignKey(Verbo, on_delete=models.CASCADE)
	id_area = models.ForeignKey(Areas, on_delete=models.CASCADE)
	dicas_objetivos = models.TextField('Dicas objetivo', blank=True)
	

