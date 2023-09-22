from rest_framework import viewsets
from .serialyzer import apuntesSerializer
from .models import apuntes
# Create your views here.
class apuntesViewSet(viewsets.ModelViewSet):
    queryset = apuntes.objects.all()
    serializer_class = apuntesSerializer
