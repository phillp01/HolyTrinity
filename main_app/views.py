from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Church
from .forms import PersonForm
from django.forms.models import model_to_dict
from django.urls import reverse
from django.template.loader import render_to_string

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
    return render(request, 'settings.html', {'churches': churches})


def people(request):
    people = Person.objects.all()
    return render(request, 'people.html', {'people': people})


def save_person_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            all_people = Person.objects.all()
            data['html_people_list'] = render_to_string('includes/partial_people_list.html', {'people':  all_people})
        else:
            data['form_is_valid'] = False
    context = {"form": form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def person_create(request):

    if request.method == 'POST':
        print("Person Create - Method = POST")
        form = PersonForm(request.POST)
    else:
        print("Person Create - Method = GET")
        form = PersonForm()
    return save_person_form(request, form, 'includes/partial_person_create.html')


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    print("Person = ", person.church)
    if request.method == 'POST':
        print("method = POST")
        form = PersonForm(request.POST, instance=person)
    else:
        form = PersonForm(instance=person)
        print("form =", form)
    return save_person_form(request, form, 'includes/partial_person_update.html')


# def person_update(request, slug):
#     person = Person.objects.get(slug=slug)
#     if request.method == 'POST':
#         form = PersonForm(data=request.POST, instance=person)
#         if form.is_valid():
#             form.save(commit=True)
#         return redirect(reverse('detail', args=[slug]))
#     else:
#         person_dict = model_to_dict(person)
#         form = PersonForm(person_dict)
#         return render(request, 'edit.html', {'form': form})
