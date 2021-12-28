from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('contact', views.contact, name="contact"),

]