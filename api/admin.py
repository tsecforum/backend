from django.contrib import admin
from .models import Student, Organisation, Scholarship, Application

# Register your models here.
admin.site.register(Student)
admin.site.register(Organisation)
admin.site.register(Scholarship)
admin.site.register(Application)