from  rest_framework import serializers
from  .models import Student


class Studentserilzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
