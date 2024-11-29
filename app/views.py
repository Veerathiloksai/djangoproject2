from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def siva(request):
   return  HttpResponse("<h1>Siva loves L*****</h1>")

def yella(request):
   return HttpResponse("<h1><marquee>Yella Loves Laddu</marquee></h1>")

def biodata(request):
   return HttpResponse('''
       <h2> Name is Michaelokade</h2>
        <h3>Age is @</h3>
        <img src="https://th.bing.com/th/id/OIP.xNO7JXJq-1IWmgji9sc8wAHaEL?w=283&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" alt="Img not available">''')
