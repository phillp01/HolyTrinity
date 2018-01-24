from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import WeddingForm, ReadingForm
from .models import Wedding, ServiceReadings, ServiceHymns
from main_app.models import Person
from main_app.views import save_form


def weddings(request):
    weddings = Wedding.objects.all()
    return render(request, 'weddings.html', {'html_list': weddings})


def wedding_create(request):
    if request.method == 'POST':
        form = WeddingForm(request.POST)
    else:
        form = WeddingForm()
        form.fields['minister'].queryset = Person.objects.filter(role=2) #Shows only Ministers
    return save_form(request, form, 'includes/partial_wedding_create.html', 'includes/partial_wedding_list.html', Wedding)


def wedding_update(request, pk):
    wedding = get_object_or_404(Wedding, pk=pk)
    if request.method == 'POST':
        readings = ServiceReadings.objects.filter(wedding_id=pk)
        hymns = ServiceHymns.objects.filter(wedding_id=pk)
        wedding_form = WeddingForm(request.POST, instance=wedding)
        if wedding_form.is_valid():
            wedding_form.save()
    else:
        wedding_form = WeddingForm(instance=wedding)
        readings = ServiceReadings.objects.filter(wedding_id=pk)
        hymns = ServiceHymns.objects.filter(wedding_id=pk)
    return render(request, 'wedding_details.html', {'wedding': wedding_form, 'readings': readings, 'hymns': hymns, 'wedding_id': wedding})


def wedding_delete(request, pk):
    wedding = get_object_or_404(Wedding, pk=pk)
    data = dict()
    if request.method == 'POST':
        wedding.delete()
        data['form_is_valid'] = True
        weddings = Wedding.objects.all()
        data['html_list'] = render_to_string('includes/partial_wedding_list.html', {'html_list': weddings})
    else:
        context = {'wedding': wedding}
        data['html_form'] = render_to_string('includes/partial_wedding_delete.html', context, request=request,)
    return JsonResponse(data)


def reading_create(request, pk):
    data = dict()
    if request.method == 'POST':
        form = ReadingForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            readings = ServiceReadings.objects.filter(wedding_id=pk)
            data['html_reading_list'] = render_to_string('includes/partial_readings_list.html', {'readings': readings})
        else:
            data['form_is_valid'] = False
    else:
        form = ReadingForm(initial={'wedding': pk})
    context = {'form': form, 'wedding_id': pk}
    data['html_form'] = render_to_string('includes/partial_reading_create.html',
        context,
        request=request)
    return JsonResponse(data)


def reading_delete(request, pk):
    reading = get_object_or_404(ServiceReadings, pk=pk)
    data = dict()
    if request.method == 'POST':
        reading.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        readings = ServiceReadings.objects.filter(wedding_id=reading.wedding_id)
        data['html_reading_list'] = render_to_string('includes/partial_readings_list.html', {
            'readings': readings
        })
    else:
        context = {'reading': reading}
        data['html_form'] = render_to_string('includes/partial_reading_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def reading_update(request, pk):
    reading = get_object_or_404(ServiceReadings, pk=pk)
    if request.method == 'POST':
        form = ReadingForm(request.POST, instance=reading)
    else:
        form = ReadingForm(instance=reading)
    return save_reading_form(request, form, 'includes/partial_reading_update.html', reading)


def save_reading_form(request, form, template_name, reading):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            readings = ServiceReadings.objects.filter(wedding_id=reading.wedding_id)
            data['html_reading_list'] = render_to_string('includes/partial_readings_list.html', {
                'readings': readings
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def hymn_create(request,pk):
    pass