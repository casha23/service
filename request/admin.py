from django.contrib import admin

from .models import Invoice, Request


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('master', 'request', 'price', 'status')


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_model', 'problem_description', 'status')
