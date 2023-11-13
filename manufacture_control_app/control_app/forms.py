from django import forms

from manufacture_control_app.control_app.models import Machine


class MachineCreateForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'machine_name',
            'number_of_tools',
            'description',
        ]


class MachineEditForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'machine_name',
            'number_of_tools',
            'description',
        ]
