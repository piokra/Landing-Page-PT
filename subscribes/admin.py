from django.contrib import admin

# Register your models here.

from .models import Subscription, Post

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ['email','timestamp','updated']
	class Meta:
		model = Subscription

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Post)
