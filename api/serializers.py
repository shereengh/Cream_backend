from rest_framework import serializers
from .models import Icecream

class IcecreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icecream
        fields = "__all__"