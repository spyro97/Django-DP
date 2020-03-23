from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('xml/<int:pk>/', views.xml_doc, name='xml_doc'),
]