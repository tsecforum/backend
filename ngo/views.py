from django.shortcuts import render
from django.http import HttpResponse
from .models import NGO,Event,Volunteer,Donation
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from .models import Volunteer

# Create your views here.
def dashboard(request):
	
	events = Event.objects.order_by('-post_date')
	list_events = []
	for event in events :
		dict_event = {
			'id':event.id,
			'title':event.title,
			'ngo':{
				'title': event.ngo.title,
				'phone_number': event.ngo.phone_number
			},
			'photo_main':"https://serene-brushlands-85477"+event.photo_main.url,
			'category':event.category,
			'description':event.description,
			'location':event.location,
			'actual_url':event.actual_url
		}
		list_events.append(dict_event)
	return JsonResponse(list_events,safe=False)

def filter_by(request) :

	events = Event.objects.filter(category = 'education')
	events_json = serializers.serialize('json',events)

	return HttpResponse(events_json,content_type='application/json')

def volunteering(request):

	username = request.GET.get('username')
	event_id = request.GET.get('event_id')
	ngo_title = request.GET.get('ngo_title')
	
	user = User.objects.get(username=username)
	event = Event.objects.get(id = event_id)
	ngo = event.ngo

	volunteer = Volunteer(user_id=user.id,event_id=event_id,ngo_id=ngo.id)
	volunteer.save()

	return JsonResponse({'Response':'Sent'})

def donating(request):

	username = request.GET.get('username')
	event_id = request.GET.get('event_id')
	ngo_title = request.GET.get('ngo_title')

	amount = request.GET.get('amount')

	user = User.objects.get(username=username)
	event = Event.objects.get(id=event_id)
	ngo = event.ngo

	donation = Donation(user_id=user.id,event_id=event.id,ngo_id=ngo.id,amount=amount)
	donation.save()

	return JsonResponse({'Donation':'Successful'})

def return_donations(request):

	username = request.GET.get('username')
	user = User.objects.get(username=username)

	donations = Donation.objects.filter(user_id=user.id)
	list_donations = []

	for donation in donations :
		dict_donation = {
			'event' : donation.event.title,
			'ngo' : donation.ngo.title,
			'amount' : donation.amount
		}
		list_donations.append(dict_donation)

	return JsonResponse(list_donations,safe=False)

