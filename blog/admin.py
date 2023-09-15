from django.contrib import admin
from .models import CustomUser, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','owner']
    list_filter = ['owner']
    search_fields = ['owner']
    



# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Blog, BlogAdmin)

