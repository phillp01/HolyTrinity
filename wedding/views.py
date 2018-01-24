from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .forms import WeddingForm, ReadingForm
from .models import Wedding, ServiceReadings, ServiceHymns
from main_app.models import Person
from main_app.views import save_form
# Create your views here.

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
    print("Wedding Update Run for wedding:", pk)
    wedding = get_object_or_404(Wedding, pk=pk)
    print("Wedding = ", wedding.id)
    if request.method == 'POST':
        print("Wedding update is POST")
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
    print("Running Reading Create for wedding:", pk)
    data = dict()
    if request.method == 'POST':
        print("Reading create is POST")
        form = ReadingForm(request.POST)
        if form.is_valid():
            print("create Reading Form is Valid")
            form.save()
            data['form_is_valid'] = True
            # readings = ServiceReadings.objects.all()
            readings = get_list_or_404(ServiceReadings, pk)
            data['html_reading_list'] = render_to_string('includes/partial_readings_list.html', {'readings': readings})
        else:
            print("create reading form is NOT valid")
            data['form_is_valid'] = False
    else:
        form = ReadingForm()
    context = {'form': form}
    data['html_form'] = render_to_string('includes/partial_reading_create.html',
        context,
        request=request)
    return JsonResponse(data)


def reading_update(request, pk):
    reading = get_object_or_404(ServiceReadings, pk=pk)
    if request.method == 'POST':
        form = ReadingForm(request.POST, instance=reading)
    else:
        form = ReadingForm(instance=reading)
    return save_reading_form(request, form, 'includes/partial_reading_update.html', reading)


def save_reading_form(request, form, template_name, reading):
    print("Save reading form run")
    print("Wed ID=", reading.wedding_id)
    data = dict()
    if request.method == 'POST':
        print("Save reading form - is POST")
        if form.is_valid():
            print("Save reading form is Valid")
            form.save()
            data['form_is_valid'] = True
            # readings = ServiceReadings.objects.all()
            readings = ServiceReadings.objects.filter(wedding_id=reading.wedding_id)
            print(readings)
            # readings = get_list_or_404(ServiceReadings, wedding_id=pk)
            print("1")
            data['html_reading_list'] = render_to_string('includes/partial_readings_list.html', {
                'readings': readings
            })
            print("2")
        else:
            print("Save reading form - is not Valid")
            data['form_is_valid'] = False
    context = {'form': form}
    print("3")
    data['html_form'] = render_to_string(template_name, context, request=request)
    print("4")
    return JsonResponse(data)
