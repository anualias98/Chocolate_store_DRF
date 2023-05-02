from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Chocolate


class ChocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields = '__all__'

