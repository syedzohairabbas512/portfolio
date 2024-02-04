from django.contrib import admin
from syed.models import Contact, Project


# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class AdminProject(admin.ModelAdmin):
    list_display = ['title', 'deploy_url', 'github_url']


admin.site.register(Contact, AdminContact)
admin.site.register(Project, AdminProject)
