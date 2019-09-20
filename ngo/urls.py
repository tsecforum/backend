from django.urls import path

from . import views

urlpatterns = [
	path('',views.dashboard,name='dashboard'),
	path('volunteering/',views.volunteering,name = 'volunteering'),
	path('donating/',views.donating,name = 'donating')
]