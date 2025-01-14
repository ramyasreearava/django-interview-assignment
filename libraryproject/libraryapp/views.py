from django.shortcuts import render
from .models import *
# Create your views here.
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

class LibrarianRegistration(generics.GenericAPIView):
    serializer_class = LibrarianSerializer
    def post(self,request):
        serailizer=self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        user=serailizer.save()
        return Response({'Message': 'Updated successful',
                         'Result': LibrarianSerializer(user).data,
                         'HasError': 'False',
                         'status': 200})


class LibrarianLogin(generics.GenericAPIView):
    serializer_class = LibrarianLoginSerializer

    def post(self,request):
        username = request.data.get('Username')
        password = request.data.get('Password')
        if Librarian.objects.filter(Username=username).first():
            user = Librarian.objects.filter(Username=username).first()
            if check_password(password, user.Password):
                x = LibrarianSerializer(user).data
                return Response({'Message': 'Login Successful',
                                 'Result': x,
                                 'HasError': 'False',
                                 'status': 200})

            else:
                return Response({'Message': 'please check the password',
                             'Result': [],
                             'HasError': 'True',
                             'status': 400})
        else:
            return Response({'Message': 'please check the username',
                             'Result': [],
                             'HasError': 'True',
                             'status': 400})



class MemberRegistration(generics.GenericAPIView):
    serializer_class = MemberSerializer
    def post(self,request):
        serailizer=self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        user=serailizer.save()
        return Response({'Message': 'Registration Successful',
                         'Result': MemberSerializer(user).data,
                         'HasError': 'False',
                         'status': 200})


class MemberLogin(generics.GenericAPIView):
    serializer_class = MemberLoginSerializer

    def post(self,request):
        username = request.data.get('Username')
        password = request.data.get('Password')
        if Member.objects.filter(Username=username).first():
            user = Member.objects.filter(Username=username).first()
            if check_password(password, user.Password):
                x = MemberSerializer(user).data,
                return Response({'Message': 'Login Successful',
                                 'Result': x,
                                 'HasError': 'False',
                                 'status': 200})

            else:
                return Response({'Message': 'please check the password',
                             'Result': [],
                             'HasError': 'True',
                             'status': 400})
        else:
            return Response({'Message': 'please check the username',
                             'Result': [],
                             'HasError': 'True',
                             'status': 400})


class Getallmembers(generics.GenericAPIView):
    serializer_class = MemberSerializer
    def get(self,request):
        result=Member.objects.all()
        serializer=MemberSerializer(result,many=True)
        return Response({'Message': 'Successful',
                         'Result': serializer.data,
                         'HasError': 'False',
                         'status': 200})

class UpdateMembers(generics.GenericAPIView):
    serializer_class = UpdateMemberSerializer
    def put(self,request,id):
        result=Member.objects.get(id=id)
        serializer=UpdateMemberSerializer(result,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Message': 'Update Successful',
                         'Result': serializer.data,
                         'HasError': 'False',
                         'status': 200})


class DeleteMembers(generics.GenericAPIView):
    serializer_class = MemberSerializer
    def delete(self,request,id):
        result=Member.objects.get(id=id)
        result.delete()
        return Response({'Message': 'Deleted Successful',
                         'Result': [],
                         'HasError': 'False',
                         'status': 200})