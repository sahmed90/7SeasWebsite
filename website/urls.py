from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about_us.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('contact_us.html', views.contact, name="contact")

]
