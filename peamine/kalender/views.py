from django.shortcuts import render

# Create your views here.


from django.http.response import HttpResponse
 
 
def home_page_view(request):
   return render(request,"LandingPage.html")

def login_page_view(request):
   return render(request, "index.html", "style.css")