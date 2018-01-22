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
    wedding = get_object_or_404(Wedding, pk=pk)
    if request.method == 'POST':
        wedding_form = WeddingForm(request.POST, instance=wedding)
        if wedding_form.is_valid():
            wedding_form.save()
    else:
        wedding_form = WeddingForm(instance=wedding)
        readings = ServiceReadings.objects.filter(wedding_id=pk)
        hymns = ServiceHymns.objects.filter(wedding_id=pk)
    return render(request, 'wedding_details.html', {'wedding': wedding_form, 'readings': readings, 'hymns': hymns})


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
