from django.urls import path

from . import views

urlpatterns = [
    path('date', views.date, name='date'),
    path('add/<int:n1>/<int:n2>', views.add, name='add'),
    path('sub/<int:n1>/<int:n2>', views.sub, name='sub'),
]