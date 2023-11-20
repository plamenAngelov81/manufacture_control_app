from django import forms

from manufacture_control_app.control_app.models import Machine, Tool, Operations


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


class ToolCreateForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = [
            'tool_name',
            'tool_length',
            'tool_diameter',
            'operation',
            'machine',
        ]


class ToolEditForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = [
            'tool_name',
            'tool_length',
            'tool_diameter',
            'operation',
            'machine',
        ]


class OperationCreateForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = '__all__'


class OperationEditForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = '__all__'
