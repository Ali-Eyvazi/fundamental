from django.shortcuts import render
from django.views import View



class HomeViwe(View):

    def get(self,request):
        return render (request,'home/home.html')
    def post(self,request):
        pass