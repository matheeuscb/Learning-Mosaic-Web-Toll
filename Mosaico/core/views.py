#-*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse #, JsonResponse
from django.db.models import Count
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import Group
# from django.contrib.auth.models import User
from django.contrib import messages
from Mosaico.core.models import Canvas, Mosaico, Objetivos_De_Aprendizagem, Nivel, Verbo, Status, Usuario, Areas

#from flask import Flask, render_template, request, redirect


def home(request):
	return render(request, 'home.html')


def dashboard(request):

	if(request.user.is_authenticated()):
		return render(request, 'blank.html')
	else:
		return render(request, 'home.html')

def contato(request):
	return render(request, 'contato.html')
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
			#if user.has_perm('admin.educador'):
			return redirect('dashboard/inicio_dashboard.html')

		else:
			messages.add_message(request, messages.ERROR, 'Login/Senha Incorretos! Confira as Informações e Tente Novamente')
			return redirect('/')

	return render(request, 'home.html')


def logout(request):
	auth_logout(request)
	return redirect('home')

def criar_canvas(request):
	
	if(request.user.is_authenticated()):
		return render(request, 'criar_canvas.html')
	else:
		return render(request, 'home.html')

	


def inicio_dashboard(request):
	if(request.user.is_authenticated()):
		return render(request, 'inicio_dashboard.html')
	else:
		return render(request, 'home.html')


def criar_canvas(request):
	if(request.user.is_authenticated()):
		if (request.method == 'POST'):
			nome_canvas = request.POST ['nome_canvas']
			descricao_canvas = request.POST ['descricao_canvas']
			id_usuario = request.user

			canvas = Canvas(nome_canvas=nome_canvas, descricao_canvas=descricao_canvas, id_usuario=id_usuario)
			# if canvas:
			try:
				canvas.save()
				messages.add_message(request, messages.SUCCESS, 'Canvas Salvo Com Sucesso!')
				return redirect('dashboard/listagem_canvas.html')
			# canvas = None

			# print nome_canvas,descricao_canvas,id_usuario

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Salvar Canvas!')

		return render(request, 'criar_canvas.html')


	else:
		return render(request, 'home.html')


def listagem_canvas(request):
	if(request.user.is_authenticated()):
		data = {'canvas': Canvas.objects.filter(id_usuario_id=request.user.id)}

		return render(request, 'listagem_canvas.html', data)

	else:
		return render(request, 'home.html')

def listagem_areas(request,id_canvas):
	if(request.user.is_authenticated()):
		data = {'canvas': Canvas.objects.get(id=id_canvas), 'areas': Areas.objects.filter(id_canvas_id=id_canvas)}

		return render(request, 'listagem_areas.html', data)

	else:
		return render(request, 'home.html')

def criar_area(request,id_canvas):

	if(request.user.is_authenticated()):
		if (request.method == 'POST'):
			nome_area = request.POST ['nome_area']
			dicas_area = request.POST ['dicas_area']
			id_canvas = id_canvas

			area = Areas(nome_area=nome_area, dicas_area=dicas_area, id_canvas_id=id_canvas)
			
			try:
				area.save()
				messages.add_message(request, messages.SUCCESS, 'Área Salva Com Sucesso!')
				url='/dashboard/listagem_areas.html/'+str(id_canvas)
				return redirect(url)

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Salvar Área!')	

		return render(request, 'criar_area.html', {'canvas': Canvas.objects.get(id=id_canvas)})


	else:
		return render(request, 'home.html')


def editar_area(request,id_area):

	if(request.user.is_authenticated()):
		if (request.method == 'POST'):
			area = Areas.objects.get(id=id_area)
			area.nome_area = request.POST ['nome_area']
			area.dicas_area = request.POST ['dicas_area']
			
			try:
				area.save()
				messages.add_message(request, messages.SUCCESS, 'Área Editada Com Sucesso!')
				url='/dashboard/listagem_areas.html/'+str(area.id_canvas_id)
				return redirect(url)

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Salvar Área!')

		return render(request, 'editar_area.html', {'area': Areas.objects.get(id=id_area)})


	else:
		return render(request, 'home.html')

def excluir_area(request,id_area):

	if(request.user.is_authenticated()):
		area = Areas.objects.get(id=id_area)
		canvas = Canvas.objects.get(id=area.id_canvas_id)
		if(canvas.id_usuario_id==request.user.id):
			try:
				area.delete()
				messages.add_message(request, messages.SUCCESS, 'Área Excluida Com Sucesso!')

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Excluir Área!')

		url='/dashboard/listagem_areas.html/'+str(area.id_canvas_id)
		return redirect(url)

	else:
		return render(request, 'home.html')




def editar_canvas(request,id_canvas):

	if(request.user.is_authenticated()):
		data = {'canvas': Canvas.objects.get(id=id_canvas)}

		if (request.method == 'POST'):
			canvas = Canvas.objects.get(id=id_canvas)

			canvas.nome_canvas=(request.POST['nome_canvas'])
			canvas.descricao_canvas=(request.POST['descricao_canvas'])


			try:
				canvas.save()
				messages.add_message(request, messages.SUCCESS, 'Canvas Editado Com Sucesso!')
				return redirect('dashboard/listagem_canvas.html')

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Editar Canvas!')


		return render(request, 'editar_canvas.html', data)

	else:
		return render(request, 'home.html')




def excluir_canvas(request,id_canvas):

	if(request.user.is_authenticated()):
		canvas = Canvas.objects.get(id=id_canvas)
		if(canvas.id_usuario_id==request.user.id):
			
			try:
				canvas.delete()
				messages.add_message(request, messages.SUCCESS, 'Canvas Excluído Com Sucesso!')

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Excluir Canvas!')

		return redirect('dashboard/listagem_canvas.html')

	else:
		return render(request, 'home.html')
	

def listagem_mosaicos(request):
	if(request.user.is_authenticated()):
		data = {'canvas': Canvas.objects.all(), 'mosaico': Mosaico.objects.filter(id_usuario_id=request.user.id)}

		#dados = {'mosaico': Mosaico.objects.filter(id_usuario_id=request.user.id)}

		return render(request, 'listagem_mosaicos.html', data)

	else:
		return render(request, 'home.html')

def pegar_verbos(request):
	id_nivel = request.GET.get('id_nivel',None)
	data = {'verbos': Verbo.objects.filter(id_nivel=id_nivel)}

	return JsonResponse(data)

def criar_mosaico(request):
	if(request.user.is_authenticated()):
		data = {'status': Status.objects.all(), 'canvas': Canvas.objects.all(), 'mosaicos': Mosaico.objects.filter(id_usuario_id=request.user.id)}
		
		lista = []

		for m in data['mosaicos']:
			lista.append(m.id_canvas.id)

		data['lista_m']=lista

		if (request.method == 'POST'):
			id_canvas = request.POST ['id_canvas']
			id_usuario = request.user.id

			mosaico = Mosaico(id_canvas_id=id_canvas, id_usuario_id=id_usuario)
			# if canvas:
			try:
				mosaico.save()
				messages.add_message(request, messages.SUCCESS, 'Mosaico Salvo Com Sucesso!')
				return redirect('listagem_mosaicos')
			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Salvar Mosaico!')

	return render(request, 'criar_mosaico.html', data)

def criar_objetivo(request, id_mosaico):
	if(request.user.is_authenticated()):

		data = {'area': Areas.objects.all(), 'status': Status.objects.all(), 'canvas': Canvas.objects.all(),'mosaico': Mosaico.objects.filter(id=id_mosaico)}

		param = dict().fromkeys(Nivel.objects.all())

		for nivel in param:
			param[nivel]=Verbo.objects.filter(id_nivel=nivel.id)

		# for nivel in param:
		# 	print nivel.tipo_nivel
		# 	for verbo in param[nivel]:
		# 		print verbo.nome_verbo

		data['drop'] = param 

		if (request.method == 'POST'):
			descricao_objetivos = request.POST ['descricao_objetivos']
			status_inicial = request.POST ['status_inicial']
			# status_final = request.POST ['status_final']
			# id_mosaico = request.POST ['id_mosaico']
			id_area = request.POST ['id_area']
			id_verbo = request.POST ['id_verbo']
			dicas_objetivos = request.POST ['dicas_objetivos']

			objetivo = Objetivos_De_Aprendizagem(descricao_objetivos=descricao_objetivos, status_inicial_id=status_inicial, status_final_id=status_inicial, id_mosaico_id=id_mosaico, id_verbo_id=id_verbo, id_area_id=id_area, dicas_objetivos=dicas_objetivos)
			# if canvas:
			# print id_verbo,'oi'
			try:
				objetivo.save()
				# return redirect('dashboard/criar_objetivo.html')
				messages.add_message(request, messages.SUCCESS, 'Objetivo Salvo Com Sucesso!')
				aux = Mosaico.objects.filter(id=id_mosaico)
				url='/dashboard/listagem_mural.html/'+str(aux[0].id_canvas_id)
				return redirect(url)
				# canvas = None

				#print nome_canvas,descricao_canvas,id_usuario
				# data = dict().fromkeys(Nivel.objects.all())
				# for nivel in data:
				# 	data[nivel]=Verbo.objects.filter(tipo_nivel=nivel)

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Salvar Objetivo!')
		
		return render(request, 'criar_objetivo.html', data)

	else:
		return render(request, 'home.html')



def listagem_mural(request,id_canvas):
	if(request.user.is_authenticated()):

		# lista = "select * from core_objetivos_de_aprendizagem as 'obj' inner join core_mosaico as 'mosaico' on mosaico.id=obj.id_mosaico_id where mosaico.id_canvas_id=%s and mosaico.id_usuario_id=%s"
		lista ="select obj.id, obj.descricao_objetivos, obj.id_verbo_id, obj.status_final_id, obj.status_inicial_id from core_objetivos_de_aprendizagem as 'obj' inner join core_mosaico as 'mosaico' on mosaico.id=obj.id_mosaico_id where mosaico.id_canvas_id=%s and mosaico.id_usuario_id=%s"
		outros = "select obj.id, obj.descricao_objetivos, obj.id_verbo_id, obj.status_final_id, obj.status_inicial_id from core_objetivos_de_aprendizagem as 'obj' inner join core_mosaico as 'mosaico' on mosaico.id=obj.id_mosaico_id where mosaico.id_canvas_id=%s and mosaico.id_usuario_id!=%s"

		data = {'canvas': Canvas.objects.get(id=id_canvas), 'mosaico': Mosaico.objects.filter(id_usuario_id=request.user.id).filter(id_canvas=id_canvas), 
		'objetivos': Objetivos_De_Aprendizagem.objects.raw(lista,[id_canvas,request.user.id]), 'outros': Objetivos_De_Aprendizagem.objects.raw(outros,[id_canvas,request.user.id]),
		'auxiliar': Mosaico.objects.all()}

		# print data['objetivos'][0].id
		# print data['objetivos'][1].id

		return render(request, 'listagem_mural.html', data)

	else:
		return render(request, 'home.html')

def excluir_objetivo(request,id_objetivo):

	if(request.user.is_authenticated()):
		obj= Objetivos_De_Aprendizagem.objects.get(id=id_objetivo)
		mosaico= Mosaico.objects.get(id=obj.id_mosaico_id)
		if(mosaico.id_usuario_id==request.user.id):
			try:
				obj.delete()
				messages.add_message(request, messages.SUCCESS, 'Objetivo Excluído Com Sucesso!')

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Excluir Objetivo!')


		url='/dashboard/listagem_mural.html/'+str(mosaico.id_canvas_id)
		return redirect(url)

		# return redirect('dashboard/listagem_mosaicos.html')

	else:
		return render(request, 'home.html')

def editar_objetivo(request,id_objetivo):

	if(request.user.is_authenticated()):

		# data = {'area': Areas.objects.all(), 'status': Status.objects.all(), 'canvas': Canvas.objects.all(),'mosaico': Mosaico.objects.filter(id=id_mosaico)}
		data = {'area': Areas.objects.all(), 'objetivo': Objetivos_De_Aprendizagem.objects.get(id=id_objetivo)}
		param = dict().fromkeys(Nivel.objects.all())

		for nivel in param:
			param[nivel]=Verbo.objects.filter(id_nivel=nivel.id)

		# for nivel in param:
		# 	print nivel.tipo_nivel
		# 	for verbo in param[nivel]:
		# 		print verbo.nome_verbo

		data['drop'] = param 

		obj= Objetivos_De_Aprendizagem.objects.get(id=id_objetivo)
		mosaico= Mosaico.objects.get(id=obj.id_mosaico_id)
		if(mosaico.id_usuario_id==request.user.id):
			if (request.method == 'POST'):
				objetivo = Objetivos_De_Aprendizagem.objects.get(id=id_objetivo)

				objetivo.dicas_objetivos =(request.POST['dicas_objetivos'])
				if (objetivo.status_final_id!= request.POST['status_final']):
					objetivo.status_final_id=(request.POST['status_final'])
					# status_final 
					# id_mosaico
					# id_verbo
				try:
					objetivo.save()
					
					messages.add_message(request, messages.SUCCESS, 'Objetivo Editado Com Sucesso!')

					url='/dashboard/listagem_mural.html/'+str(mosaico.id_canvas_id)
					return redirect(url)
					
				except:

					messages.add_message(request, messages.ERROR, 'Erro ao Salvar Objetivo!')
					return render(request, 'editar_objetivo.html', data)
				
				# return redirect('dashboard/listagem_mosaicos.html')

		return render(request, 'editar_objetivo.html', data)

	else:
		return render(request, 'home.html')


def registro(request):
	if (request.method == 'POST'):
			name = request.POST ['name']
			lastname = request.POST ['lastname']
			username = request.POST ['email']
			password = request.POST ['password']
			tipo= request.POST ['tipo']
			imagem = request.FILES['imagem']

			usu = Usuario(name=name, lastname=lastname, email=username,imagem=imagem)
			try:
				usu.set_password(password)
				usu.save()
				usu = Usuario.objects.get(email=username)
				tipo = Group.objects.get(id=tipo)
				usu.groups.add(tipo)
				messages.add_message(request, messages.SUCCESS, 'Usuário Criado Com Sucesso! Faça Login!')
				

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Criar Usuário! Tente Novamente!')

			return redirect('home')

def perfil(request):

	if(request.user.is_authenticated()):
		if (request.method == 'POST'):

			user = request.user

			user.name=(request.POST['name'])
			user.lastname=(request.POST['lastname'])
			if (user.email != request.POST['email']):
				user.email=(request.POST['email'])
			if (user.password != request.POST['password']):
				user.set_password(request.POST['password'])
			try:
				user.imagem=(request.FILES['imagem'])
			except:
				pass
			try:
				user.save()
				user.groups.clear()
				user.groups.add(request.POST['tipo'])
				messages.add_message(request, messages.SUCCESS, 'Perfil Editado Com Sucesso!')
				return redirect('perfil')

			except:
				messages.add_message(request, messages.ERROR, 'Erro ao Editar Perfil!')

		return render(request, 'perfil.html')

	else:
		return render(request, 'home.html')

def relatorios(request):
	if(request.user.is_authenticated()):
		return render(request, 'relatorios.html')
	else:
		return render(request, 'home.html')

def relatorio_canvas(request):

	if(request.user.is_authenticated()):
		data = {'canvas': Canvas.objects.filter(id_usuario_id=request.user.id)}

		return render(request, 'relatorio_canvas.html', data)

	else:
		return render(request, 'home.html')

def grafico3(request):
	# id_canvas='7'
	# lista ="select objt.id, objt.status_final_id, count(objt.status_final_id) as qtde from core_objetivos_de_aprendizagem as objt inner join core_mosaico as mosaico on mosaico.id=objt.id_mosaico_id inner join core_canvas as canvas on canvas.id=mosaico.id_canvas_id where mosaico.id_canvas_id=%s group by status_final_id"
	# objetivos = list (Objetivos_De_Aprendizagem.objects.raw(lista,[id_canvas]))
	
	# # # cont = list (Objetivos_De_Aprendizagem.objects.raw(lista))	
	# test = {'status': json.dumps([objt.status_final.nome_status for objt in objetivos]), 'qtde': json.dumps([objt.qtde for objt in objetivos])}
	# print objetivos
	# print test

	if(request.user.is_authenticated()):
		sql = "select id, status_final_id, count(status_final_id) as qtde from core_objetivos_de_aprendizagem group by status_final_id"

		contador = list (Objetivos_De_Aprendizagem.objects.raw(sql))

		data = {'status': json.dumps([obj.status_final.nome_status for obj in contador]), 'qtde': json.dumps([obj.qtde for obj in contador])}

		# print data
		# print contador
		return render(request, 'grafico3.html', data)

	else:
		return render(request, 'home.html')

def pegar_areas(request):
	id_canvas = '7'
	print "oi"
	data = {'areas': Areas.objects.filter(id_canvas_id=id_canvas)}

	return JsonResponse(data)

def mural (request):

	id_canvas = '7'

	lista ="select obj.id, obj.descricao_objetivos, obj.id_verbo_id, obj.status_final_id, obj.status_inicial_id from core_objetivos_de_aprendizagem as 'obj' inner join core_mosaico as 'mosaico' on mosaico.id=obj.id_mosaico_id where mosaico.id_canvas_id=%s and mosaico.id_usuario_id=%s"
	outros = "select obj.id, obj.descricao_objetivos, obj.id_verbo_id, obj.status_final_id, obj.status_inicial_id from core_objetivos_de_aprendizagem as 'obj' inner join core_mosaico as 'mosaico' on mosaico.id=obj.id_mosaico_id where mosaico.id_canvas_id=%s and mosaico.id_usuario_id!=%s"

	data = {'canvas': Canvas.objects.get(id=id_canvas), 'mosaico': Mosaico.objects.filter(id_usuario_id=request.user.id).filter(id_canvas=id_canvas), 
	'objetivos': Objetivos_De_Aprendizagem.objects.raw(lista,[id_canvas,request.user.id]), 'outros': Objetivos_De_Aprendizagem.objects.raw(outros,[id_canvas,request.user.id]),
	'auxiliar': Mosaico.objects.all(), 'areas': Areas.objects.filter(id_canvas_id=id_canvas)}

	return render(request, 'mural.html', data)

def listagem_graficos (request,id_canvas):

	data = {'canvas': Canvas.objects.get(id=id_canvas)}

	return render(request, 'listagem_graficos.html',data)

def grafico_status_final(request,id_canvas):

	if(request.user.is_authenticated()):
		lista ="select objt.id, objt.status_final_id, count(objt.status_final_id) as qtde from core_objetivos_de_aprendizagem as objt inner join core_mosaico as mosaico on mosaico.id=objt.id_mosaico_id inner join core_canvas as canvas on canvas.id=mosaico.id_canvas_id where mosaico.id_canvas_id=%s group by status_final_id"
		objetivos = list (Objetivos_De_Aprendizagem.objects.raw(lista,[id_canvas]))

		data = {'status': json.dumps([objt.status_final.nome_status for objt in objetivos]), 'qtde': json.dumps([objt.qtde for objt in objetivos])}
		# print objetivos
		# print data
		return render(request, 'grafico_status_final.html', data)

	else:
		return render(request, 'home.html')

def grafico_status_inicial(request,id_canvas):

	if(request.user.is_authenticated()):
		lista ="select objt.id, objt.status_inicial_id, count(objt.status_inicial_id) as qtde from core_objetivos_de_aprendizagem as objt inner join core_mosaico as mosaico on mosaico.id=objt.id_mosaico_id inner join core_canvas as canvas on canvas.id=mosaico.id_canvas_id where mosaico.id_canvas_id=%s group by status_inicial_id"
		objetivos = list (Objetivos_De_Aprendizagem.objects.raw(lista,[id_canvas]))

		data = {'status': json.dumps([objt.status_inicial.nome_status for objt in objetivos]), 'qtde': json.dumps([objt.qtde for objt in objetivos])}
		print objetivos
		print data
		return render(request, 'grafico_status_inicial.html', data)

	else:
		return render(request, 'home.html')

def grafico_dimensao(request,id_canvas):

	if(request.user.is_authenticated()):
		lista ="select objt.id, verbo.id_nivel_id, nivel.tipo_nivel, count(objt.id_verbo_id) as qtde from core_objetivos_de_aprendizagem as objt inner join core_mosaico as mosaico on mosaico.id=objt.id_mosaico_id inner join core_canvas as canvas on canvas.id=mosaico.id_canvas_id  inner join core_verbo as verbo on verbo.id=objt.id_verbo_id inner join core_nivel as nivel on nivel.id=verbo.id_nivel_id  where mosaico.id_canvas_id=%s group by id_nivel_id"
		objetivos = list (Objetivos_De_Aprendizagem.objects.raw(lista,[id_canvas]))

		data = {'dimensao': json.dumps([objt.tipo_nivel for objt in objetivos]), 'qtde': json.dumps([objt.qtde for objt in objetivos])}
		print objetivos
		# print data
		# print objt.id_verbo_id.id_nivel_id.tipo_nivel
		return render(request, 'grafico_dimensao.html', data)

	else:
		return render(request, 'home.html')

