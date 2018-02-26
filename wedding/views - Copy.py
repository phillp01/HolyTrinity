from django.apps import apps
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.six import iteritems
from django.db import models
import datetime
from .forms import WeddingForm, ReadingForm, HymnForm
#from .models import Wedding, ServiceReading, ServiceHymn, additionalServices
from .models import Wedding, ServiceReading, ServiceHymn
from main_app.models import Person,Church
from main_app.views import save_form, person_create

from decimal import *

get_model = apps.get_model

def weddings(request):
    weddings = Wedding.objects.all()
    return render(request, 'weddings.html', {'html_list': weddings})

# def index1(request):
    # services_choices=additionalServices.objects.all().count()
    # return render(
        # request,
        # 'index.html',
        # context={'services_choices':services_choices},
    # )

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


def total_wedding_amount(request):
    id_wedding = 3;
    model = 'Church'   
    app = 'main_app'
    total_amount = Decimal(0.00)
    model_class = get_model(app, model)
 
    by_license = request.POST['checked_array[0][by_license]']
    choir = request.POST['checked_array[1][choir]']
    organ = request.POST['checked_array[2][organ]']
    bells = request.POST['checked_array[3][bells]']
    flowers = request.POST['checked_array[4][flowers]']
    video = request.POST['checked_array[5][video]']
    cd = request.POST['checked_array[6][cd]']
    winter_heating = request.POST['checked_array[7][winter_heating]']
    verger = request.POST['checked_array[8][verger]']
    car_park_attendant = request.POST['checked_array[9][car_park_attendant]']
	
    id_church = request.POST['id_church']	
	
    #all_data = list(Church.objects.values())
    all_data = list(Church.objects.filter(id=id_church).values())
    
	
    now=datetime.datetime.now().date()
	
    if all_data[0]['statutory_upcoming_date'] > now:
        total_amount = total_amount + all_data[0]['statutory_current_price']
    else:
        total_amount = total_amount + all_data[0]['statutory_upcoming_price']
	
    if by_license == '1':
        total_amount = total_amount + all_data[0]['by_license']
  
    if choir == '1':
        total_amount = total_amount + all_data[0]['choir']
  
    if organ == '1':
        total_amount = total_amount + all_data[0]['organ']
  
    if bells == '1':
        total_amount = total_amount + all_data[0]['bells']
  
    if flowers == '1':
        total_amount = total_amount + all_data[0]['flowers']
  
    if video == '1':
        total_amount = total_amount + all_data[0]['video']
  
    if cd == '1':
        total_amount = total_amount + all_data[0]['cd']
  
    if winter_heating == '1':
        total_amount = total_amount + all_data[0]['winter_heating']
  
    if verger == '1':
        total_amount = total_amount + all_data[0]['verger']
  
    if car_park_attendant == '1':
        total_amount = total_amount + all_data[0]['car_park_attendant']
		
        total_amount = total_amount + all_data[0]['by_license']
		
    if id_wedding:
        model = 'Wedding'
        app = 'wedding'
        wedding_data = list(Wedding.objects.filter(id=id_wedding).values())

    if wedding_data[0]['by_license_price']=='0.0000':
        by_license_price = wedding_data[0]['by_license_price'];		
    else:by_license_price = all_data[0]['by_license'];
	
    if wedding_data[0]['video_price']=='0.0000':
        video_price = wedding_data[0]['video_price'];		
    else:video_price = all_data[0]['video'];

    if wedding_data[0]['cd_price']=='0.0000':
        cd_price = wedding_data[0]['cd_price'];		
    else:cd_price = all_data[0]['cd'];

    if wedding_data[0]['winter_heating_price']=='0.0000':
        winter_heating_price = wedding_data[0]['winter_heating_price'];		
    else:winter_heating_price = all_data[0]['winter_heating'];

    if wedding_data[0]['organ_price']=='0.0000':
        organ_price = wedding_data[0]['organ_price'];		
    else:organ_price = all_data[0]['organ'];

    if wedding_data[0]['choir_price']=='0.0000':
        choir_price = wedding_data[0]['choir_price'];		
    else:choir_price = all_data[0]['choir'];

    if wedding_data[0]['bells_price']=='0.0000':
        bells_price = wedding_data[0]['bells_price'];		
    else:bells_price = all_data[0]['bells'];

    if wedding_data[0]['flowers_price']=='0.0000':
        flowers_price = wedding_data[0]['flowers_price'];		
    else:flowers_price = all_data[0]['flowers'];

    if wedding_data[0]['verger_price']=='0.0000':
        verger_price = wedding_data[0]['verger_price'];		
    else:verger_price = all_data[0]['verger'];

    if wedding_data[0]['car_park_attendant_price']=='0.0000':
        car_park_attendant_price = wedding_data[0]['car_park_attendant_price'];		
    else:car_park_attendant_price = all_data[0]['car_park_attendant'];
	
    if wedding_data[0]['church_price']=='0.0000':
        church_price = wedding_data[0]['church_price'];		
    else:
        if all_data[0]['statutory_upcoming_date'] > now:
            church_price = all_data[0]['statutory_current_price']
        else:
            church_price = all_data[0]['statutory_upcoming_price']
			
    data = [{'total_amount':total_amount},{'church_price':church_price},{'car_park_attendant_price':car_park_attendant_price}]
	        		
        
    return HttpResponse(total_amount)