from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import FileResponse, HttpResponse
from .models import Bills
from .tables import SimpleTable
from .filters import BillsFilter
import xml.etree.cElementTree as ET


def report_list(request):
    bills = Bills.objects.all()
    myFilter = BillsFilter(request.GET, queryset=bills)
    bills = myFilter.qs
    table = SimpleTable(bills)
    table.paginate(page=request.GET.get("page", 1), per_page=12)
    return render(request, 'reportes/report_list.html', {'table': table, 'myFilter':myFilter})


def xml_doc(request, pk):
    data = get_object_or_404(Bills, pk=pk)
    print(data)
    print(data.xml)
    id= data.id
    root = ET.fromstring(data.xml)
    print(root)
    doc = ET.SubElement(root, "doc")
    tree = ET.ElementTree(root)
    tree.write("xml/xml-"+str(id)+".xml")
    response = HttpResponse(open("xml/xml-"+str(id)+".xml", 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=xml'+str(id)+'.xml'
    return response
    
