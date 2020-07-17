from django.contrib import admin

# Register your models here.
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    search_fields = ["email"]


admin.site.register(Subscriber, SubscriberAdmin)
