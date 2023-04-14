from django.contrib import admin
from  feeds.models import feed_fun
# Register your models here.
class serv_admin(admin.ModelAdmin):
    list_display=('name','location','message')
admin.site.register(feed_fun,serv_admin)