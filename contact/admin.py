from django.contrib import admin

from contact.models import  admincontact, publiccontact

# Register your models here.
admin.site.register(publiccontact)

admin.site.register(admincontact)