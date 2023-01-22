from django.contrib import admin

from .models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_model', 'problem_description', 'status')

admin.site.register(Request, RequestAdmin)