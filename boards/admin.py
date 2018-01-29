from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Board, Topic, Post


# Register your models here.
class BoardAdmin(ModelAdmin):
    pass


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, BoardAdmin)
admin.site.register(Post, BoardAdmin)
