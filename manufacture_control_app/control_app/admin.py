from django.contrib import admin

from manufacture_control_app.control_app.models import Machine, Tool, Operations, OrderParts


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    pass


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass


@admin.register(Operations)
class OperationsAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderParts)
class OrderPartsAdmin(admin.ModelAdmin):
    pass
