from logging import exception
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions

from users.authentication import generate_access_token
from .models import User
from .serializers import UserSerializer
@api_view(['POST'])
def register(request):
    data=request.data
    if data['password'] != data['confirm_password']:
        raise exceptions.APIException("Passwords do not match")
    else:
        serialzer = UserSerializer(data=data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        return Response(serialzer.data)

@api_view(["POST"])
def login(request):
    email=request.data.get("email")
    password=request.data.get("password")

    user= User.objects.filter(email=email).first()
    
    if user is None:
        raise exceptions.AuthenticationFailed("User not found!")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Wrong password")

    response= Response()
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data={
        "jwt":token
    }
    return response


    

@api_view(['GET'])
def user(request):
    
    serialzer = UserSerializer(User.objects.all(),many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def hello(request):
    
    return Response("hey")