from django.shortcuts import render

# Create your views here.


from django.http.response import HttpResponse
 
 
def home_page_view(request):
<<<<<<< HEAD
   return render(request,"LandingPage.html")

def login_page_view(request):
   return render(request, "index.html", "style.css")
=======
   return render(request, "LandingPage.html")
>>>>>>> 01859356cf6cc78ad9011b3b93a650ada92a0f2d
