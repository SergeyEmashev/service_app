from django.contrib import admin

from services.models import Service, Plan, Subscrition

# Register your models here.
admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscrition)