from django.contrib import admin

from .models import Invoice, Request


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('master', 'request', 'price', 'status')

admin.site.register(Invoice, InvoiceAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_model', 'problem_description', 'status')

admin.site.register(Request, RequestAdmin)
