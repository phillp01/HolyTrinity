from django.shortcuts import render, redirect
from .models import Person, Church
from .forms import PersonForm
from django.forms.models import model_to_dict
from django.urls import reverse
# Create your views here.


def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


def detail(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'detail.html', {'person':person})


def edit(request, slug):
    person = Person.objects.get(slug=slug)
    if request.method == 'POST':
        form = PersonForm(data=request.POST, instance=person)
        if form.is_valid():
            form.save(commit=True)
        return redirect(reverse('detail', args=[slug]))
    else:
        person_dict = model_to_dict(person)
        form = PersonForm(person_dict)
        return render(request, 'edit.html', {'form': form})


def settings(request):
    churches = Church.objects.all()
    return render(request, 'settings.html', {'churches': churches})


def people(request):
    people = Person.objects.all()
    return render(request, 'people.html', {'people': people})
