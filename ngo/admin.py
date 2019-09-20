from django.contrib import admin
from .models import NGO,Event,Volunteer,Donation
# Register your models here.
class NGOAdmin(admin.ModelAdmin):

	list_display = ('id','title','is_verified','post_date')
	list_display_links = ('id','title')
	list_editable = ('is_verified',)
	search_fields = ('title','description')

admin.site.register(NGO,NGOAdmin)

class EventAdmin(admin.ModelAdmin):

	list_display = ('id','title','location','category','post_date','amount')
	list_display_links = ('id','title')
	search_fields = ('title','description','location')

admin.site.register(Event,EventAdmin)

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('user','event','ngo')
	list_display_links = ()
	search_fields = ('ngo__title',)

admin.site.register(Volunteer,VolunteerAdmin)

class DonationAdmin(admin.ModelAdmin):
	list_display = ('user','event','ngo','amount')
	list_display_links = ()
	search_fields = ('ngo__title',)

admin.site.register(Donation,DonationAdmin)