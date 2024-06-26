from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from datetime import timedelta

from .forms import (
    InspectionTemplateForm, InspectionGroupsForm, InspectionForm, 
    InspectionResponseFormSet
)
from. models import *


def add_template(request):
    templates = InspectionTemplate.objects.all().values('id', 'name').order_by('name')
    if request.method == 'POST':
        form = InspectionTemplateForm(request.POST)
        if form.is_valid():
            inspection_template = form.save()

            if form.cleaned_data['create_inspections']:
                inspection = Inspection.objects.create(
                    name=inspection_template.name, 
                    template=inspection_template
                )

                messages.success(
                    request,
                    f'''
                        Template criado com sucesso!<br/> 
                        Link temporário da inspeção: 
                        <a href="http://195.200.4.149/inspection/answer_inspection/{inspection.id}">http://195.200.4.149/inspection/answer_inspection/{inspection.id}<a>''',
                )
            return redirect('add_template')
    else:
        form = InspectionTemplateForm()
        
    return render(
        request, 
        'inspection/add_template.html',
        {
            'form': form,
            'templates': templates,
        }
    )

def add_group(request):
    if request.method == 'POST':
        form = InspectionGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_template')
    else:
        form = InspectionGroupsForm()
        
    return render(
        request, 
        'inspection/add_group.html',
        {
            'form': form,
        }
    )

def add_inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save()


            messages.success(
                    request,
                    f'''
                        Inspeção criada com sucesso!<br/> 
                        Link temporário da inspeção: 
                        <a href="http://195.200.4.149/inspection/answer_inspection/{inspection.id}">http://195.200.4.149/inspection/answer_inspection/{inspection.id}<a>''',
                )
            return redirect('add_inspection')
    else:
        form = InspectionForm()
        
    return render(
        request, 
        'inspection/add_inspection.html',
        {
            'form': form,
        }
    )

def answer_inspection(request, pk):
    inspection = get_object_or_404(Inspection, id=pk)
    inspection_responses = InspectionResponse.objects.filter(
        inspection=inspection
    )

    if timezone.now() - inspection.created_at >= timedelta(hours=2):
        return render(request, 'inspection/inspection_expirated.html')

    if request.method == 'POST':
        formset = InspectionResponseFormSet(request.POST, request.FILES, queryset=inspection_responses)
        if formset.is_valid():
            formset.save()
            return redirect('answer_inspection', inspection.id)
    else:
        formset = InspectionResponseFormSet(queryset=inspection_responses)
    
    return render(
        request, 
        'inspection/answer_inspection.html', 
        {'form': formset, 'inspection_name': inspection.name,}
        )
