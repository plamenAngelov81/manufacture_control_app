from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy
from manufacture_control_app.control_app.forms import MachineCreateForm, MachineEditForm, ToolCreateForm, \
    ToolEditForm, OperationCreateForm, OperationEditForm
from manufacture_control_app.control_app.models import Machine, Tool, Operations


def index(request):
    return render(request, 'control_templates/index.html')


class GetMachinesView(generic.ListView):
    model = Machine
    template_name = 'control_templates/machines/get_machines.html'


class MachineCreateView(generic.CreateView):
    model = Machine
    form_class = MachineCreateForm
    template_name = 'control_templates/machines/machine_create.html'
    success_url = reverse_lazy('get machines')


class MachineDetailsView(generic.DetailView):
    model = Machine
    template_name = 'control_templates/machines/machine_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tools = Tool.objects.filter(machine_id=self.object.pk)
        context["tools"] = tools
        return context


class MachineEditView(generic.UpdateView):
    model = Machine
    form_class = MachineEditForm
    template_name = 'control_templates/machines/machine_edit.html'

    def get_success_url(self):
        return reverse_lazy('machine details', kwargs={
            'pk': self.object.pk
        })


class GetToolsView(generic.ListView):
    model = Tool
    template_name = 'control_templates/tools/get_tools.html'


class ToolCreateView(generic.CreateView):
    model = Tool
    form_class = ToolCreateForm
    template_name = 'control_templates/tools/tool_create.html'
    success_url = reverse_lazy('get tools')


class ToolDetailsView(generic.DetailView):
    model = Tool
    template_name = 'control_templates/tools/tool_details.html'


class ToolEditView(generic.UpdateView):
    model = Tool
    form_class = ToolEditForm
    template_name = 'control_templates/tools/tool_edit.html'

    def get_success_url(self):
        return reverse_lazy('tool details', kwargs={
            'pk': self.object.pk
        })


class GetOperationView(generic.ListView):
    model = Operations
    template_name = 'control_templates/operations/get_operation.html'


class OperationCreateView(generic.CreateView):
    model = Operations
    form_class = OperationCreateForm
    template_name = 'control_templates/operations/operation_create.html'
    success_url = reverse_lazy('get operations')


class OperationDetailsView(generic.DetailView):
    model = Operations
    template_name = 'control_templates/operations/operation_details.html'


class OperationEditView(generic.UpdateView):
    model = Operations
    form_class = OperationEditForm
    template_name = 'control_templates/operations/operation_edit.html'

    def get_success_url(self):
        return reverse_lazy('operation details', kwargs={
            'pk': self.object.pk
        })
