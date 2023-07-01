from django.contrib import admin
from  .models import Register



class Registerlist(admin.ModelAdmin):
    list_display = ["username","email"]



admin.site.register(Register,Registerlist)





