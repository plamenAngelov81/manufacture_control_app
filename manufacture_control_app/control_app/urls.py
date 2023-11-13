from django.urls import path, include

from manufacture_control_app.control_app.views import index, MachineCreateView, GetMachinesView, MachineDetailsView, MachineEditView

urlpatterns = [
    path('', index, name='index'),
    path('machines/', include([
        path('', GetMachinesView.as_view(), name='get machines'),
        path('create/', MachineCreateView.as_view(), name='create machine'),
        path('<int:pk>/machine-details', MachineDetailsView.as_view(), name='machine details'),
        path('<int:pk>/machine-edit', MachineEditView.as_view(), name='machine edit'),
    ])),
]
