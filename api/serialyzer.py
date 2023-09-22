from rest_framework import serializers
from .models import apuntes
class apuntesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apuntes
        fields = ('__all__')