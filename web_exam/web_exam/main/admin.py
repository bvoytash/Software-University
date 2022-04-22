from django.contrib import admin

# Register your models here.
from web_exam.main.models import Profile, Game

admin.site.register(Profile)
admin.site.register(Game)