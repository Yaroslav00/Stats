from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Point

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')




class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model=Point
        fields = ['x', 'y']

# class PointGetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LinearRegresion
#         fields = ['alpha']