import csv
import io
import json
from tkinter import Canvas
from django.contrib import admin

from account.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import FileResponse, HttpResponse, JsonResponse

from django.urls import path


# Register your models here.
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export CSV"

@admin.register(User)
class userAdmin(admin.ModelAdmin, ExportCsvMixin):
 
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'avatar')}),
        (('Permissions'), {'fields': ('is_approved', 'is_deny',  'is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions', 'is_heriages', 'is_arts','is_media', 'is_creation', 'is_artscrafts',
                                       'is_fastival', 'is_celebrations', 'is_historical', 'is_museums', 'is_libraries', 'is_archives',
                                       'is_painting', 'is_digital', 'is_photography', 'is_sculpture', 'is_pottery', 'is_livemusic', 'is_theater',
                                       'is_dance', 'is_opera', 'is_puppetry', 'is_book', 'is_magazines', 'is_comics', 'is_film', 'is_television',
                                       'is_radio', 'is_musicvideo', 'is_digitalcontent', 'is_software', 'is_videogames', 'is_animations',
                                       'is_fashion', 'is_jewellery', 'is_toys', 'is_interiordesign', 'is_graphics', 'is_architecture', 'is_advertising',
                                       'is_creativerd', 'is_creativeeventservices', 'is_digitalservices')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ["date_joined"]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('id','email',  'is_approved', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
    search_fields = ('id','email', 'first_name', 'last_name')
    ordering = ('email',)
    actions = ["export_as_csv"]
  

    
# class CustomUserAdmin(UserAdmin):
#     """Define admin model for custom User model with no username field."""
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (('Personal info'), {'fields': ('first_name', 'last_name', 'avatar')}),
#         (('Permissions'), {'fields': ('is_approved','is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions', 'is_heriages', 'is_arts','is_media', 'is_creation')}),
#         (('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     readonly_fields = ["date_joined"]
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('id','email',  'is_approved', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
#     search_fields = ('id','email', 'first_name', 'last_name')
#     ordering = ('email',)

#     change_list_template = 'change_list_graph.html'

    
# admin.site.register(get_user_model(), CustomUserAdmin)



   


# import json

# from django.contrib import admin
# from django.core.serializers.json import DjangoJSONEncoder
# from django.db.models import Count
# from django.db.models.functions import TruncDay
# from django.http import JsonResponse
# from django.urls import path




# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('id','email',  'is_approved', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
#     search_fields = ('id','email', 'first_name', 'last_name')
#     ordering = ("-date_joined",)
#     change_list_template = 'change_list_graph.html'
#     # Inject chart data on page load in the ChangeList view
#     def changelist_view(self, request, extra_context=None):
#         chart_data = self.chart_data()
#         as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
#         extra_context = extra_context or {"chart_data": as_json}
#         return super().changelist_view(request, extra_context=extra_context)

#     def get_urls(self):
#         urls = super().get_urls()
#         extra_urls = [
#             path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
#         ]
#         # NOTE! Our custom urls have to go before the default urls, because they
#         # default ones match anything.
#         return extra_urls + urls

#     # JSON endpoint for generating chart data that is used for dynamic loading
#     # via JS.
#     def chart_data_endpoint(self, request):
#         chart_data = self.chart_data()
#         return JsonResponse(list(chart_data), safe=False)

#     def chart_data(self):
#         return (
#             User.objects.annotate(date=TruncDay("date_joined"))
#             .values("date")
#             .annotate(y=Count("id"))
#             .order_by("-date")
#         )


   