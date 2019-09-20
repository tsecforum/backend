from django.shortcuts import render
from django.http import HttpResponse
from .models import NGO,Event
from django.core import serializers
from django.http import JsonResponse,HttpResponse

# Create your views here.
def dashboard(request):
	
	events = Event.objects.order_by('-post_date')
	list_events = []
	for event in events :
		dict_event = {
			'title':event.title,
			'ngo':{
				'title': event.ngo.title,
				'phone_number': event.ngo.phone_number
			},
			'photo_main':"https://serene-brushlands-85477"+event.photo_main.url,
			'category':event.category,
			'description':event.description
		}
		list_events.append(dict_event)
	return JsonResponse(list_events,safe=False)
	

	return HttpResponse(events_json,content_type='application/json')

def filter_by(request) :

	events = Event.objects.filter(category = 'education')
	events_json = serializers.serialize('json',events)

	return HttpResponse(events_json,content_type='application/json')

