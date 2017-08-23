from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')


def contato(request):
	return render(request, 'contato.html')


def login(request):
	return render(request, 'login.html')


def logout(request):
	return render(request, 'home.html')