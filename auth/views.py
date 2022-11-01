from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)



@csrf_exempt
@permission_classes((AllowAny,))
def slogin(request):
   if request.method == "POST":
       data2 = JSONParser().parse(request)
       username = data2["username"]
       password = data2["password"]
       print(username,password)
       if username=="" or password =="":
           return JsonResponse({'error': 'Please provide both username and password'},
                           status=HTTP_400_BAD_REQUEST)
       user = authenticate(username=username, password=password)
       if not user:
           return JsonResponse({'error': 'Invalid Credentials'},
                           status=HTTP_404_NOT_FOUND)
       else:
           login(request,user)
           request.session['email'] = user.email
           token, _ = Token.objects.get_or_create(user=user)
           return JsonResponse({'token': token.key,"massage":"logged in successfuly",'first_name':user.first_name,'last_name':user.last_name,'username':user.username,'email':user.email}, status=HTTP_200_OK)



