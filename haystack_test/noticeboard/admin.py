from django.contrib import admin
from noticeboard.models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass

