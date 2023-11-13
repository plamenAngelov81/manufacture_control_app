from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy
from manufacture_control_app.control_app.forms import MachineCreateForm, MachineEditForm
from manufacture_control_app.control_app.models import Machine


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


class MachineEditView(generic.UpdateView):
    model = Machine
    form_class = MachineEditForm
    template_name = 'control_templates/machines/machine_edit.html'

    def get_success_url(self):
        return reverse_lazy('machine details', kwargs={
            'pk': self.object.pk
        })
