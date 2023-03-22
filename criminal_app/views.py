from django.shortcuts import render, redirect
from .models import Criminal
from django.contrib import messages
 


# Create your views here.
def home(request):
    records = Criminal.objects.all().order_by('-pk')
    return render(request, 'home.html', {'records': records})


def add_record(request):
    criminal_obj = Criminal()
    criminal_obj.name = request.POST.get('name')

    criminal_obj.criminal_number = request.POST.get('criminal_number')
    criminal_obj.nickname = request.POST.get('nickname')
    criminal_obj.address = request.POST.get('address')
    criminal_obj.date_of_crime = request.POST.get('date_of_crime')
    criminal_obj.arrest_date = request.POST.get('arrest_date')
    criminal_obj.occupation = request.POST.get('occupation')
    criminal_obj.crime_type = request.POST.get('crime_type')
    criminal_obj.age = request.POST.get('age')
    criminal_obj.fathers_name = request.POST.get('fathers_name')
    criminal_obj.gender = request.POST.get('gender')

    criminal_obj.wanted = request.POST.get('wanted')
    criminal_obj.criminal_image = request.FILES.get('criminal_image')

    criminal_obj.save()
    messages.success(request, 'Successfully Added Criminal Record.')
    return redirect('/')


def update_record(request, pk):
    criminal_obj = Criminal.objects.get(pk=pk)
    criminal_obj.name = request.POST.get('name')

    criminal_obj.criminal_number = request.POST.get('criminal_number')
    criminal_obj.nickname = request.POST.get('nickname')
    criminal_obj.address = request.POST.get('address')
    criminal_obj.date_of_crime = request.POST.get('date_of_crime')
    criminal_obj.arrest_date = request.POST.get('arrest_date')
    criminal_obj.occupation = request.POST.get('occupation')
    criminal_obj.crime_type = request.POST.get('crime_type')
    criminal_obj.age = request.POST.get('age')
    criminal_obj.fathers_name = request.POST.get('fathers_name')
    criminal_obj.gender = request.POST.get('gender')

    criminal_obj.wanted = request.POST.get('wanted')
    
    if request.FILES.get('criminal_image'):
        criminal_obj.criminal_image = request.FILES.get('criminal_image')

    criminal_obj.save()
    messages.success(request, 'Successfully Updated Criminal Record.')
    return redirect('/')


def delete_record(request, pk):
    criminal_obj = Criminal.objects.get(pk=pk)
    criminal_obj.delete()
    messages.success(request, 'Successfully Deleted Criminal Record.')
    return redirect('/')