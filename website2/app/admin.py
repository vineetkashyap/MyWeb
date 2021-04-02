from django.contrib import admin
from app.models import Blog,OurTeam
# Register your models here.
@admin.register(Blog)
class BlodAdmin(admin.ModelAdmin):
    list_display = ['id','title','posted_by','description','blog_image','blog_date']
@admin.register(OurTeam)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','wing','description','facebook','linkedin','twitter']
