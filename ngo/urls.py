from django.urls import path

from . import views

urlpatterns = [
	path('',views.dashboard,name='dashboard'),
	path('volunteering/',views.volunteering,name = 'volunteering'),
	path('donating/',views.donating,name = 'donating'),
	path('ret_donations/',views.return_donations,name='return_donations'),
	path('details/',views.show_ngos,name='show_ngos')
]