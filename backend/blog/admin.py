from django.contrib import admin

from blog.models import *


@admin.register(Post)  # reg app
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Application)  # reg app
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SocialItem)
class SocialItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
