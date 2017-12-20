
from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('list/<int:page>/', views.list, name="list"),
    path('item/<int:id>/', views.main, name="item"),
]