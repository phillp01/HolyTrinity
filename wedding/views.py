from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist


from .forms import WeddingForm, ReadingForm, HymnForm
from .models import Wedding, ServiceReading, ServiceHymn
from main_app.models import Person
from main_app.views import save_form, person_create


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
        readings = ServiceReading.objects.filter(wedding_id=pk)
        hymns = ServiceHymn.objects.filter(wedding_id=pk)
        wedding_form = WeddingForm(request.POST, instance=wedding)
        if wedding_form.is_valid():
            wedding_form.save()
    else:
        wedding_form = WeddingForm(instance=wedding)
        readings = ServiceReading.objects.filter(wedding_id=pk)
        hymns = ServiceHymn.objects.filter(wedding_id=pk)
        try:
            groom = Person.objects.get(wedding_id=pk, role='Groom')
        except ObjectDoesNotExist:
            groom = None
        try:
            bride = Person.objects.get(wedding_id=pk, role='Bride')
        except ObjectDoesNotExist:
            bride = None
        print("Groom = ", groom)
        print("Bride =", bride)
    return render(request, 'wedding_details.html', {'wedding': wedding_form, 'readings': readings, 'hymns': hymns, 'wedding_id': wedding, 'groom': groom, 'bride': bride})


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
        data['html_form'] = render_to_string('includes/partial_wedding_delete.html', context, request=request, )
    return JsonResponse(data)


def reading_create(request, pk):
    data = dict()
    if request.method == 'POST':
        form = ReadingForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            readings = ServiceReading.objects.filter(wedding_id=pk)
            data['html_reading_list'] = render_to_string(
                'includes/partial_readings_list.html', {'readings': readings})
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
    reading = get_object_or_404(ServiceReading, pk=pk)
    data = dict()
    if request.method == 'POST':
        reading.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        readings = ServiceReading.objects.filter(wedding_id=reading.wedding_id)
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
    reading = get_object_or_404(ServiceReading, pk=pk)
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
            readings = ServiceReading.objects.filter(wedding_id=reading.wedding_id)
            data['html_reading_list'] = render_to_string(
                'includes/partial_readings_list.html', {
                'readings': readings
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def hymn_create(request, pk):
    print("Hymn Create run")
    data = dict()
    if request.method == 'POST':
        print("Hymn Create is POST")
        form = HymnForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            hymns = ServiceHymn.objects.filter(wedding_id=pk)
            data['html_reading_list'] = render_to_string(
                'includes/partial_hymns_list.html', {'hymns': hymns})
        else:
            data['form_is_valid'] = False
    else:
        form = HymnForm(initial={'wedding': pk})
    context = {'form': form, 'wedding_id': pk}
    data['html_form'] = render_to_string('includes/partial_hymn_create.html',
                                         context,
                                         request=request)
    return JsonResponse(data)


def hymn_update(request, pk):
    hymn = get_object_or_404(ServiceHymn, pk=pk)
    if request.method == 'POST':
        form = HymnForm(request.POST, instance=hymn)
    else:
        form = HymnForm(instance=hymn)
    return save_hymn_form(request, form, 'includes/partial_hymn_update.html', hymn)


def hymn_delete(request, pk):
    print("Hymn Delete Run")
    hymn = get_object_or_404(ServiceHymn, pk=pk)
    data = dict()
    if request.method == 'POST':
        print("Hymn delete is POST")
        hymn.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        hymns = ServiceHymn.objects.filter(wedding_id=hymn.wedding_id)
        data['html_reading_list'] = render_to_string(
            'includes/partial_hymns_list.html', {
            'hymns': hymns
        })
    else:
        print("Hymn delete is NOT POST")
        context = {'hymn': hymn}
        data['html_form'] = render_to_string('includes/partial_hymn_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def save_hymn_form(request, form, template_name, hymn):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            hymns = ServiceHymn.objects.filter(wedding_id=hymn.wedding_id)
            data['html_reading_list'] = render_to_string(
                'includes/partial_hymns_list.html', {
                'hymns': hymns
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def bride_create(request, pk):
    print("Bride create run with wedding id = ", pk)
    person_create(request, pk)
    # return HttpResponse("<h1>GOGOGO</h1>")
