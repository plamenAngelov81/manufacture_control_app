from django.urls import path, include

from manufacture_control_app.control_app.views import index, MachineCreateView, GetMachinesView, MachineDetailsView, \
    MachineEditView, GetToolsView, ToolCreateView, ToolDetailsView, ToolEditView

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
        path('<int:pk>/machine-details', ToolDetailsView.as_view(), name='tool details'),
        path('<int:pk>/machine-edit', ToolEditView.as_view(), name='tool edit'),
    ]))
]
