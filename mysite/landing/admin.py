from django.contrib import admin

# Register your models here.
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name']
    search_fields = ['email','name']
admin.site.register(Subscriber, SubscriberAdmin)
