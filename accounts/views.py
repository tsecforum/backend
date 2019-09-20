from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile

# Create your views here.
@csrf_exempt
def register(request) :
	first_name = request.POST['name']
	username = request.POST['username']
	email = request.POST['email']
	contact_number = request.POST['contact_number']
	password = request.POST['password']
	password2 = request.POST['password2']
	dic = {'register':'unsuccessful','error':'no error'}

	if password == password2 :
		if User.objects.filter(username = username).exists():
			#send error
			dic['error'] = "Username already exists"
			return JsonResponse(dic)
		else :
			if User.objects.filter(email = email).exists():
				#send error
				dic['error'] = "Email id already exists"
				return JsonResponse(dic)
			else :
				user = User.objects.create_user(username = username,password = password,email = email,first_name = name,last_name = last_name)
				user.save()
				auth.login(request,user)
				dic['register'] = 'successful'
				return JsonResponse(dic)
	else :
		dic['error'] = "Password didn't match"
		return son_response(dic)

@csrf_exempt
def login(request) :

#	if request.method == 'POST':
	username = request.POST['username']
	password = request.POST['password']

	dic = {'login':'unsuccessful','error':'Invalid Credentials'}
	user = auth.authenticate(username = username,password = password)

	if user is not None :
		auth.login(request,user)
		dic['login'] = 'successful'
		dic['error'] = 'no error'
		return JsonResponse(dic)
	else :
		return JsonResponse(dic)
#	else :
#		return render(request,'login.html')

@csrf_exempt
def logout(request):
	auth.logout(request)
	dic = {'logout':'successful'}
	return JsonResponse(dic)

def send_profile(request):

	user = request.user
	profile = Profile.objects.get(user = user.id)
	dic = {
		'id' : user.id,
		'first_name' : user.first_name,
		'username' : user.username,
		'phone number' : profile.contact_no,
		'email id' : user.email
	}
	return JsonResponse(dic)