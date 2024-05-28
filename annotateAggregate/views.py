from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Order, Seller


def AAview(request):
    result = Seller.objects.all()
    print(result.values_list("name"))
    return HttpResponse(f'Resultado: {result.values_list("name")[0]}')


# Create your views here.
