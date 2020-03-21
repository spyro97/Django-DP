from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('list', views.report_list2, name='report_list2'),
    path('xml/<int:pk>/', views.xml_doc, name='xml_doc'),
    path('report_search/<int:pk>/', views.report_search, name='report_search'),
]