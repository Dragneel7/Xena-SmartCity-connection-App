from django.contrib import admin
from .models import *

admin.site.register(UserProfile)

class TagInline(admin.StackedInline):
    model = Tag
    extra=5


class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['org_name']}),
        ('Tag information', {'fields': ['org_desc'], 'classes': ['collapse']}),
    ]
    inlines = [TagInline]

admin.site.register(Organisation,OrganisationAdmin)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3


class ViewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['view']}),]
    inlines = [CommentInline]

admin.site.register(View, ViewAdmin)
