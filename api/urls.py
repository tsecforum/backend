from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('post/organisation/', views.post_organisation, name='post_organisation'),
    path('get/organisation/', views.get_organisation, name='get_organisation'),
    path('post/student/', views.post_student, name='post_student'),
    path('get/student/', views.get_student, name='get_student'),
    path('post/scholarship/', views.post_scholarship, name='post_scholarship'),
    path('get/scholarship/', views.get_scholarship, name='get_scholarship'),
    path('get/type/', views.get_type, name='get_type'),
    path('get/scholarship/eligible/', views.get_scholarship_eligible, name='get_scholarship_eligible'),
    path('get/scholarship/organisation/', views.get_scholarship_organisation, name='get_scholarship_organisation'),
    path('get/scholarship/details/', views.get_scholarship_details, name='get_scholarship_details'),
    path('get/scholarship/application/', views.get_scholarship_application, name='get_scholarship_application'),
    path('get/scholarship/filter/', views.get_scholarship_filter, name='get_scholarship_filter'),
    path('post/scholarship/apply/', views.post_scholarship_apply, name='post_scholarship_apply'),
    path('post/application/status/', views.post_application_status, name='post_application_status'),
]
