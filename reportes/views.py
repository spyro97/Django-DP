from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import FileResponse, HttpResponse
from .models import Bills
import xml.etree.cElementTree as ET

def report_list(request):
    bills = Bills.objects.all()
    return render(request, 'reportes/report_list.html', {'bills':bills})

def xml_doc(request, pk):
    data = get_object_or_404(Bills, pk=pk)
    root = ET.fromstring(data.xml)
    doc = ET.SubElement(root, "doc")
    tree = ET.ElementTree(root)
    response = HttpResponse(open("xml-"+str(pk)+".xml", 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=xml'+str(pk)+'.xml'
    return response

def report_search(request, pk):
    bill_data = get_object_or_404(Bills, pk=pk)
    return render(request, 'reportes/report_search.html', {'bills':bill_data})
    
