from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View

# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class Home_Page(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home_page.html')

class Power_Building(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'power_building.html')
