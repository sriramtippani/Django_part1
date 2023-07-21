from django.contrib import admin
from app1.models import hydjobs, blorejobs, chennaijobs, punejobs

# Register your models here.
class hydJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']

admin.site.register(hydjobs, hydJobsAdmin)

class bloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']

admin.site.register(blorejobs, bloreJobsAdmin)

class chennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']

admin.site.register(chennaijobs, chennaiJobsAdmin)

class puneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']

admin.site.register(punejobs, puneJobsAdmin)