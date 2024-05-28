from django.urls import path
from . import views

app_name = 'annotateAggregate'

urlpatterns = [
    path('', views.AAview, name="aa")
]

