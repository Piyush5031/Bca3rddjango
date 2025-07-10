from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

class piyushlmsSignupUser(APIView):
    def post(self,request):
        userdata=piyushlmsSignupSerializer(data=request.data)
        if userdata.is_valid():
            piyushlmsUser.objects.create(**userdata.data) #ORM (Performing insert new user in lmsUser table and passing complete dictionary data i.e. kArgs)
            message={"message":"User created successfully"}
            return JsonResponse(message,status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)
    
class piyushlmsGetUserDetails(APIView):
    def get(self,request):
        result=list(piyushlmsUser.objects.filter().values()) # To fetch a list of all users from lmsUser table
        return JsonResponse(result,status=status.HTTP_200_OK,safe = False)
    
class piyushlmsUpdateEmail(APIView):
    def put(self,request):
        userdata=piyushlmsUpdateEmail(data=request.data)
        if userdata.is_valid():
            email=userdata.data["email"]
            number=userdata.data["number"]
            piyushlmsUser.objects.filter(number=number).update(email=email)
            message={"message":"Email updated successfully"}
            return JsonResponse(message,status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)
    
class piyushlmsDeleteUser(APIView):
    def delete(self,request,number):
        piyushlmsUser.objects.filter(number=number).delete()
        message={"message":"User deleted successfully"}
        return JsonResponse(message,status=status.HTTP_204_NO_CONTENT)