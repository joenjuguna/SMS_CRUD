from rest_framework import serializers
from .models import smsmodel


class smsserializer(serializers.ModelSerializer):
    class Meta:
        model = smsmodel
        fields = '__all__'
