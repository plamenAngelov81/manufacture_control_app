from django.contrib import admin

from manufacture_control_app.users.models import Employee


@admin.register(Employee)
class UserProfileAdmin(admin.ModelAdmin):
    pass