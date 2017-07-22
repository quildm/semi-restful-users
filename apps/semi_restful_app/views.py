from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index_and_create(request):
	if request.method == "POST":
		User.objects.create(first_name=request.POST['first_name'],
		last_name=request.POST['last_name'],
		email=request.POST['email']),
		return redirect('/users')
	else:
		context = {
		"all_users": User.objects.all()
		}
		return render(request,'semi_restful_app/index.html', context)

def users_new(request):
	return render(request, 'semi_restful_app/users_new.html')

def users_show_and_update(request, user_id):
	if request.method == "POST":
		the_user = User.objects.filter(id=user_id)
		the_user.update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'] )
		return redirect('/users')
	else:
		the_user = User.objects.get(id=user_id)
		context = {
		"user": the_user
		}
		return render(request, 'semi_restful_app/users_show.html', context)

def users_edit(request, user_id):
	the_user = User.objects.get(id=user_id)
	context = {
	"user": the_user
	}
	return render(request, 'semi_restful_app/users_edit.html', context)

def users_delete(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/users')