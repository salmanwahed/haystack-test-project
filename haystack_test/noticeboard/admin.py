from django.contrib import admin
from noticeboard.models import Notice

class NoticeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notice, NoticeAdmin)
