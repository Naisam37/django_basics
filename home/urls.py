from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='home'),
    path('about/',views.about, name='about'),
    path('booking/',views.bookings,name='booking'),
    path('doctors/',views.doctors,name='doctor'),
    path('contact/',views.contact,name='contact'),
    path('departments/',views.departments,name='departments'),
    path('templateinheritance/',views.template_inheritance),
    
]