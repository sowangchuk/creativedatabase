from django.contrib import admin

from app.models import   artist_profile, authUser


class AuthAdmin(admin.ModelAdmin):
     list_display = ('user',  'owner', 'cell_number','Dzongkhag', 'remarks', 'date_joined',  'is_staff', 'skills',  'document', )
     search_fields = ( 'user', 'cell_number',)
admin.site.register(authUser, AuthAdmin)

class profileadmin(admin.ModelAdmin):
     list_display = ('user', 'name','phone','pubcountry', 'pudDzongkhag', 'date_joined',  'pubskills',  'pubdocument', 'pubprofile'  )
     search_fields = ( 'user', 'phone', 'name',)
     # change_list_template = 'change_list_graph.html'
admin.site.register(artist_profile, profileadmin)


