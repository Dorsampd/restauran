from django.shortcuts import render
from .models import *
import datetime
from .models import*
# Create your views here.
def home(request):
    n=datetime.datetime.now()
    return render(request,"app/index.html",context={"CRT":n})
def about(request):
    return render(request,"app/about.html")
def booking(request):
    return render(request,"app/booking.html")
def menu(request):
    x=foods.objects.all()
    return render(request,"app/menu.html",context={"n":x})
def contact(request):
    return render(request,"app/contact.html")
def testimonial(request):
    return render(request,"app/testimonial.html")
