from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .forms import WeddingForm
from .models import Wedding

# Create your views here.

def weddings(request):
    weddings = Wedding.objects.all()
    return render(request, 'weddings.html', {'html_list': weddings})


def wedding_update(request, pk):
    wedding = get_object_or_404(Wedding, pk=pk)
    if request.method == 'POST':
        form = WeddingForm(request.POST, instance=wedding)
    else:
        form = WeddingForm(instance=wedding)
    return save_form(request, form, 'includes/partial_wedding_update.html', 'includes/partial_wedding_list.html',  Wedding)


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


def wedding_create(request):
    if request.method == 'POST':
        form = WeddingForm(request.POST)
    else:
        form = WeddingForm()
    return save_form(request, form, 'includes/partial_wedding_create.html', 'includes/partial_wedding_list.html', Wedding)


def save_form(request, form, partial_create_template_name, partial_list_template_name,  modal):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            html_list = modal.objects.all()
            data['html_list'] = render_to_string(partial_list_template_name, {'html_list':  html_list})
        else:
            data['form_is_valid'] = False
    context = {"form": form}
    data['html_form'] = render_to_string(partial_create_template_name, context, request=request)
    return JsonResponse(data)