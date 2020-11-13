from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('addEntry', views.addEntry, name='addEntry'),
    path('<int:id>',views.viewEntry,name='viewEntry'),
    path('edit/<int:id>',views.editEntry,name='editEntry'),
    path('delete/<int:id>',views.deleteEntry,name='deleteEntry'),
    path('toggleEdit',views.toggleEdit,name='toggleEdit')
]
