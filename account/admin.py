from django.contrib import admin
from .models import UserInfo, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "birth", "phone")
    list_filter = ("birth",)
    ordering = ['birth',]
    

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "school", "company", "profession", "address", "aboutme")
    list_filter = ("school", "company", "profession",)
    search_fields = ("user",)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
# Register your models here.
