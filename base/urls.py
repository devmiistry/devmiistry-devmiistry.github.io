from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('aboutme', views.aboutme),
    path('contactme', views.contactme),
    path('portfolio', views.portfolio),
    path('projects', views.projects),
]