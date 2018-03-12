from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import Person, Church
from .forms import PersonForm
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.urls import reverse


from django.http import JsonResponse
# Create your views here.

def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


def detail(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'detail.html', {'person': person})


def settings(request):
    churches = Church.objects.all()
    roles = Role.objects.all()
    context = {'churches': churches, 'roles': roles}
    return render(request, 'settings.html', context)


def people(request):
    people = Person.objects.all()
    return render(request, 'people.html', {'people': people})


def save_person_form(request, form, template_name):
    print("Save person form run")
    data = dict()
    if request.method == 'POST':
        print("Save person is POST")
        if form.is_valid():
            print("save person form - form is valid")
            form.save()
            data['form_is_valid'] = True
            all_people = Person.objects.all()
            data['html_list'] = render_to_string('includes/partial_people_list.html', {'people':  all_people})
        else:
            print("save person form - form is NOT valid")
            data['form_is_valid'] = False
    else:
        print("Save person is get")
    context = {"form": form}

    print("Context =", context)
    print("Template name =", template_name)
    # render_to_string('includes/partial_person_create.html', context, request=request)
    data['html_form'] = render_to_string(template_name, context, request=request)
    # data['html_form'] = "<div>hello</div>"

    return JsonResponse(data)

    # return HttpResponse("HELLO")


def person_create(request):
    if request.method == 'POST':
        print("request is POST")
        form = PersonForm(request.POST)
    else:
        print("request is get")
        form = PersonForm()
    return save_person_form(request, form, 'includes/partial_person_create.html')


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
    else:
        form = PersonForm(instance=person)
    return save_person_form(request, form, 'includes/partial_person_update.html')


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    data = dict()
    if request.method == 'POST':
        person.delete()
        data['form_is_valid'] = True
        people = Person.objects.all()
        data['html_list'] = render_to_string('includes/partial_people_list.html', {'people': people})
    else:
        context = {'person': person}
        data['html_form'] = render_to_string('includes/partial_person_delete.html', context, request=request,)
    return JsonResponse(data)


def save_form(request, form, partial_create_template_name, partial_list_template_name,  modal):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            html_list = modal.objects.all()
            print(html_list)
            data['html_list'] = render_to_string(partial_list_template_name, {'html_list':  html_list})
        else:
            data['form_is_valid'] = False
    context = {"form": form}
    data['html_form'] = render_to_string(partial_create_template_name, context, request=request)
    return JsonResponse(data)
