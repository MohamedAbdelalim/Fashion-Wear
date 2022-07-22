from django.shortcuts import render, redirect
from requests import request
from multiprocessing import context
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Category, Product, Cart
from .serializers import RegistrationSerializer, CategorySerializer, ProductSerializer, UserSerializer, CartSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .forms import CreateUserForm
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import login,logout,authenticate
from rest_framework_simplejwt.models import TokenUser
from .serializers import MyTokenObtainPairSerializer, MyTokenObtainPairView
from rest_framework_simplejwt.tokens import Token

def registerPage(request):
    if request.user.is_authenticated:
        
        return redirect('index')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:

        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username,password=password)
    
        # token = MyTokenObtainPairSerializer.get_token(username)
        # JWTAuthentication[username,token].authenticate(request)
        return redirect('index')

    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)
            if user is not None:
                #token = MyTokenObtainPairSerializer.get_token(user)
                #TokenUser.save(token)
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    context = {
        'items':Product.objects.all()
    }
    return render(request, 'home-page.html', context)


def product(request):
    return render(request, 'product-page.html')


def checkout(request):

    return render(request,'checkout-page.html')


#def Product(req)

class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(generics.ListCreateAPIView):    
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer    

