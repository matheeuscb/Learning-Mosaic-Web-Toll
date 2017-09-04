from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

#from flask import Flask, render_template, request, redirect


def home(request):
	return render(request, 'home.html')


def contato(request):
	return render(request, 'contato.html')

def dashboard(request):

	if(request.user.is_authenticated()):
		return render(request, 'blank.html')
	else:
		return render(request, 'home.html')

def sobre(request):
	return(render(request, 'index2.html'))

def teste(request):
	return render(request, 'index3.html')

def lgteste(request):

	if (request.method == 'POST'):
		usuario = request.POST ['username']
		senha = request.POST ['password']

		print usuario,senha

		user = authenticate(username=usuario, password=senha)
		#usu = User()
		#usu.set_password(senha)
		#usu.username(usuario)
		#user = authenticate(usu)

		if user is not None:
			auth_login(request,user)
			#print 'oi'
			return redirect('dashboard')


	return render(request, 'lgteste.html')

#login
def login(request):

	if (request.method == 'POST'):
		usuario = request.POST ['username']
		senha = request.POST ['password']

		print usuario,senha

		user = authenticate(username=usuario, password=senha)
		#usu = User()
		#usu.set_password(senha)
		#usu.username(usuario)
		#user = authenticate(usu)

		if user is not None:
			auth_login(request,user)
			#print 'oi'
			return redirect('dashboard')



	return render(request, 'login.html')


def logout(request):
	auth_logout(request)
	return redirect('home')