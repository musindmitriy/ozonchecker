
from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list),
    path('<int:id>/', views.main),
]