from django.shortcuts import render
from .models import Genre
# Create your views here.
def home(request):
    genres=Genre.objects.all()
    return render(request,'genre/home.html',{'genres':genres})
