from django.contrib import admin

from xojiakbar.models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


