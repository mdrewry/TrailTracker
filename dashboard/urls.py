from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('addEntry', views.addEntry, name='addEntry'),
    path('feed/<int:id>/',views.viewEntry,name='viewEntry'),
    path('feed/edit/<int:id>/',views.editEntry,name='editEntry'),
]
