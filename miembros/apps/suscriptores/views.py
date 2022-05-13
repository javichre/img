from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.core.paginator import Paginator


def Home(request):
    return render(request,'index.html')


def Memberchip(request):
    return render(request,'miembros/membrecia.html')