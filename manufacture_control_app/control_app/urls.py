from django.urls import path, include

from manufacture_control_app.control_app.views import index, MachineCreateView, GetMachinesView, MachineDetailsView, \
    MachineEditView, GetToolsView, ToolCreateView, ToolDetailsView, ToolEditView, GetOperationView, \
    OperationCreateView, OperationDetailsView, OperationEditView

urlpatterns = [
    path('', index, name='index'),
    path('machines/', include([
        path('', GetMachinesView.as_view(), name='get machines'),
        path('create/', MachineCreateView.as_view(), name='create machine'),
        path('<int:pk>/machine-details', MachineDetailsView.as_view(), name='machine details'),
        path('<int:pk>/machine-edit', MachineEditView.as_view(), name='machine edit'),
    ])),
    path('tools/', include([
        path('', GetToolsView.as_view(), name='get tools'),
        path('create/', ToolCreateView.as_view(), name='create tool'),
        path('<int:pk>/tool-details', ToolDetailsView.as_view(), name='tool details'),
        path('<int:pk>/tool-edit', ToolEditView.as_view(), name='tool edit'),
    ])),
    path('operations/', include([
        path('', GetOperationView.as_view(), name='get operations'),
        path('create/', OperationCreateView.as_view(), name='create operation'),
        path('<int:pk>/tool-details', OperationDetailsView.as_view(), name='operation details'),
        path('<int:pk>/tool-edit', OperationEditView.as_view(), name='operation edit'),
    ])),
]
