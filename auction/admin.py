from django.contrib import admin

from .models import ActiveList, UserBid, UserComment, WatchList

# Register your models here.
admin.site.register(ActiveList)
admin.site.register(UserBid)
admin.site.register(UserComment)
admin.site.register(WatchList)

