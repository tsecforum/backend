from django.shortcuts import render
from django.http import HttpResponse
from .models import NGO,Event
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
	
	events = Event.objects.order_by('-post_date')
	events_json = serializers.serialize('json',qs)

	return HttpResponse(events_json,content_type='application/json')
