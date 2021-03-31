from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
	return HttpResponse("Happy Holi")
def display(request):
	return HttpResponse("hey this is guest")
def dyte(req,ru):
	return HttpResponse("Hello "+ru)
def details(req,name,age):
	return HttpResponse("Your Name is: {}</br>Your age is: {}".format(name,age))

def details1(r,age,state,sal,name):
	return HttpResponse("<h2>Your Name is:<span style='background-color:black;color:white'>{}</h2><h3>Your age is:<span style='background-color:green;color:white'> {}</h3><h4>Your state is: {}</h4>Your sal is: {}".format(name,age,state,sal))