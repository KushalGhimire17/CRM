from django.shortcuts import render
from django.http import HttpResponse
from .models import Agent, Lead


def home_page(request):
    return render(request, "home_page.html")
