from django.contrib import admin
from snippet.models import Snippet

# Register your models here.
@admin.register(Snippet)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'titel', 'code', 'languege', 'style')
