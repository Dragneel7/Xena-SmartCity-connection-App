from django.contrib import admin
from .models import *

admin.site.register(UserProfile)


admin.site.register(Organisation)
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2


class ViewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['view','userview']}),]
    inlines = [CommentInline]

admin.site.register(View, ViewAdmin)
