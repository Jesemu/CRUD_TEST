from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
	if request.user.is_authenticated():
		users_list=Usuario.objects.all()
		

		page = request.GET.get('page', 1)

		paginator = Paginator(users_list, 6)
		try:
			users_list = paginator.page(page)
		except PageNotAnInteger:
			users_list = paginator.page(1)
		except EmptyPage:
			users_list = paginator.page(paginator.num_pages)

		context = {'users_list' : users_list}
		return render(request, 'app/index.html', context)	
	else:
		return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/index.html')

def add_user(request):
	if not request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			r=form.save(commit=False)
			r.owner=request.user
			r.save()
			return redirect('/')			
	else:
		form=UserForm()
	context={'form':form}
	return render(request, 'app/add_user.html', context)


def modify_user(request, id_user):
	if not request.user.is_authenticated():
		return redirect('/')
	u=Usuario.objects.get(id=id_user)
	iban_aux=u.iban
	if request.method == 'POST':
		u.iban=0 #Not the best way.........
		u.save()
		form=UserForm(request.POST)
		if form.is_valid():
			r=form.save(commit=False)
			u.name=r.name
			u.owner=request.user
			u.surname=r.surname
			u.iban=r.iban
			u.save()
			return redirect('/')	
		else:
			u.iban=iban_aux
			u.save()		
	else:
		form=UserForm()
	context={'form':form, 'user_modifying' : u}
	return render(request, 'app/add_user.html', context)

def delete_user(request, id_user):
	if not request.user.is_authenticated():
		return redirect('/')
	u=Usuario.objects.get(id=id_user)
	context={'user_deleting' : u}
	return render(request, 'app/deleting_user.html', context)

def user_deleted(request, id_user):
	if not request.user.is_authenticated():
		return render(request, 'app/index.html')
	u=Usuario.objects.get(id=id_user)
	u.delete()
	return render(request, 'app/user_deleted.html')