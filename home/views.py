from django.shortcuts import render, HttpResponse , render
from datetime import datetime
#from home.models import Services
from home.models import home_service

# Create your views here.
def index(request):
    '''context = {
        'var1':'This is Aneeq',
        'var2':'I am a CIS Engg'}'''
    return render(request, 'index.html')
    #return HttpResponse('this is home page')

def about(request):
    #return HttpResponse('this is about page')
    return render(request, 'about.html')

def services(request):
    #return HttpResponse('this is services page')
    #print('this is request:',request.method)
    #print('this is email:',request.POST.get('email'))

    return render(request, 'services.html')

def save(request):
    if request.method == 'POST':
        print('this is email:',request.POST.get('email'))
        print('this is password:',request.POST.get('password'))
        email = request.POST.get('email')
        password = request.POST.get('password')
        services = home_service(email=email,password=password)
        print('object:',)
        services.save()

        return render(request, 'services.html')