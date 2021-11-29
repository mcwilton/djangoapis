from rest_framework import serializers
from . models import employees


class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = ('first_name', 'last_name')
    fields = '__all__'