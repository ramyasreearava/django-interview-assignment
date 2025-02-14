from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields="__all__"

    def create(self, validated_data):
        user=Librarian.objects.create(Firstname=validated_data['Firstname'],
                                     Lastname=validated_data['Lastname'],
                                     Email=validated_data['Email'],
                                     Username=validated_data['Username'],
                                     Password=make_password(validated_data['Password']),
                                     MobileNumber=validated_data['MobileNumber'])
        user.save()
        return user


class LibrarianLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=['Username','Password']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields="__all__"

    def create(self, validated_data):
        user=Member.objects.create(LibrarianId=validated_data['LibrarianId'],
                                   Firstname=validated_data['Firstname'],
                                     Lastname=validated_data['Lastname'],
                                     Email=validated_data['Email'],
                                     Username=validated_data['Username'],
                                     Password=make_password(validated_data['Password']),
                                     MobileNumber=validated_data['MobileNumber'])
        user.save()
        return user


class MemberLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=['Username','Password']

class UpdateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields="__all__"

    def update(self, instance, validated_data):
        #password=validated_data.get('Password')
        instance.LibrarianId=validated_data.get('LibrarianId')
        instance.Firstname=validated_data.get('Firstname')
        instance.Lastname=validated_data.get('Lastname')
        instance.Email=validated_data.get('Email')
        instance.Username=validated_data.get('Username')
        instance.Password = make_password('Password')
        instance.MobileNumber=validated_data.get('MobileNumber')
        instance.save()
        return instance
