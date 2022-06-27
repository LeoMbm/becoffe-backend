from django.http import HttpRequest
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from listings.models import Users
from listings.serializers import UsersSerializer

@csrf_exempt
def usersApi(request, id=0):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method=='POST':
        users_data=JSONParser.parse(request)
        users_serializer = UsersSerializer(data=users_data)
    if users_serializer.is_valid():
        users_serializer.save()
        return JsonResponse("User Add", safe=False)
         

def users(request):
    return HttpResponse('<h1>Users views</h1>')

def promo(request):
    return HttpResponse('<h1>Promo views</h1>')
    
def recipe(request):
    return HttpResponse('<h1>Recipe views</h1>')