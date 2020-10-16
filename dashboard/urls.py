from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('addEntry', views.addEntry, name='addEntry'),
    path('feed', views.feed, name='feed'),
    path('feed/<int:id>/',views.viewEntry,name='viewEntry'),
]