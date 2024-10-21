from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import admin
from .models import PizzaCard


def index(request):
    # return render(request, 'index.html')
    pizza_card = PizzaCard.objects.all()  # Получаем все пиццы из базы данных
    return render(request, 'index.html', {'pizza_card': pizza_card})

def login(request):
    return render(request, 'login.html')

def about_us(request):
    return render(request, 'about_us.html')

