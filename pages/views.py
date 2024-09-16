from django.shortcuts import render, redirect
from .models import team
from cars.models import Car
from django.contrib import messages
from django.core.mail import send_mail
from carzone.settings import EMAIL_HOST_USER
# Create your views here.
def home(request):
    teams = team.objects.all()
    featured_cars = Car.objects.all().order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.all().order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        messages.success(request, 'Your message has been submitted successfully!')
        full_message = 'Name: ' + name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nMessage: ' + message



        send_mail(subject, full_message, email, [EMAIL_HOST_USER], fail_silently=False)
        return redirect('contact')
    return render(request, 'pages/contact.html')    

def services(request):
    return render(request, 'pages/services.html')