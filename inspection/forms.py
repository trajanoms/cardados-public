from django import forms


from .models import (
    InspectionTemplate, InspectionGroup, Inspection, InspectionResponse
)

class InspectionTemplateForm(forms.ModelForm):
    create_inspections = forms.BooleanField(
        label="Gerar link temporário ao final"
    )
    class Meta:
        model = InspectionTemplate
        fields =['name', 'vehicle', 'inspection_groups']
    

class InspectionGroupsForm(forms.ModelForm):
    class Meta:
        model = InspectionGroup
        fields = ['group', 'name', 'items']


class InspectionForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=InspectionTemplate.objects.all(),
        empty_label="Selecione um template",
        required=True,
        label="Template de Inspeção",
        to_field_name="name",
    )
    class Meta:
        model = Inspection
        fields = ['name', 'template']


class InspectionResponsesForm(forms.ModelForm):
    class Meta:
        model = InspectionResponse
        fields = ['item', 'classification', 'photo',]
        widgets = {
            'item': forms.Select(attrs={'readonly': 'readonly'}),
        }

InspectionResponseFormSet = forms.modelformset_factory(
    InspectionResponse,
    form=InspectionResponsesForm,
    extra=0  # Número de formulários extra no formset (0 neste caso)
)