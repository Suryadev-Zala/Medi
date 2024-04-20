from django.contrib import admin

# Register your models here.
from .models import Images,XRayImages,info,user_info,Diabetes,chest_ct,contact_us
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# class LoginInline(admin.StackedInline):
#     model = info2
#     can_delete = False
#     verbose_name_plural = "login"


# Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [LoginInline]

admin.site.register(Images)
admin.site.register(XRayImages)
admin.site.register(info)
admin.site.register(user_info)
admin.site.register(Diabetes)
admin.site.register(chest_ct)
admin.site.register(contact_us)


admin.site.unregister(User)
# admin.site.register(User, UserAdmin)