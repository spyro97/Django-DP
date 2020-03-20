from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Bills

def report_list(request):
    bills = Bills.objects.all()
    return render(request, 'reportes/report_list.html', {'bills':bills})



