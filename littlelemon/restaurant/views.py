from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Menu
from .serializers import MenuSerializer


def index(request):
    return render(request, 'restaurant/index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer