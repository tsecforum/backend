from django.shortcuts import render
from django.http import HttpResponse
from .models import NGO,Event
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
	

	return HttpResponse(events_json,content_type='application/json')

def filter_by(request) :

	events = Event.objects.filter(category = 'education')
	events_json = serializers.serialize('json',events)

	return HttpResponse(events_json,content_type='application/json')

def volunteering(request):

	event_title = request.GET.get('event_title')
	print(event_title)
	user = request.user
	event = Event.objects.get(title = event_title)
	ngo_id = event.ngo.id
	print(ngo_id)

	volunteer = Volunteer(user.id,event.id,ngo_id)
	volunteer.save()

	return JsonResponse({'Response':'Sent'})

def donating(request):

	user = request.user
	event_title = request.GET.get('event_title')
	amount = request.GET.get('amount')
	
	event = Event.objects.get(title=event_title)
	ngo_id = event.ngo.id

	donation = Donation(user.id,event.id,ngo_id,amount)
	donation.save()

	return JsonResponse({'Donation':'Successful'})
