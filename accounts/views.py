from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile

# Create your views here.
@csrf_exempt
def register(request) :
	first_name = request.GET.get('name')
	username = request.GET.get('username')
	email = request.GET.get('email')
	contact_number = request.GET.get('contact_number')
	password = request.GET.get('password')
	password2 = request.GET.get('password2')
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
				user = User.objects.create_user(username = username,password = password,email = email,first_name = first_name)
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
	username = request.GET.get('username','')
	password = request.GET.get('password','')

	print(username,password)
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

	username = request.GET.get('username')
	user = User.objects.get(username = username)
	profile = Profile.objects.get(user = user.id)
	dic = {
		'id' : user.id,
		'first_name' : user.first_name,
		'username' : user.username,
		'phone number' : profile.contact_no,
		'email id' : user.email
	}
	return JsonResponse(dic)