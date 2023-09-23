from rest_framework import viewsets
from .serialyzer import apuntesSerializer
from rest_framework import generics
from .models import apuntes
# Create your views here.
class apuntesViewSet(viewsets.ModelViewSet):
    queryset = apuntes.objects.all()
    serializer_class = apuntesSerializer
#a delete view
class apuntesDelete(generics.DestroyAPIView):
    queryset = apuntes.objects.all()
    serializer_class = apuntesSerializer
#a update view
class apuntesUpdate(generics.UpdateAPIView):
    queryset = apuntes.objects.all()
    serializer_class = apuntesSerializer
#a create view
class apuntesCreate(generics.CreateAPIView):
    queryset = apuntes.objects.all()
    serializer_class = apuntesSerializer
    
