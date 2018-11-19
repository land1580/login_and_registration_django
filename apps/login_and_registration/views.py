from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    context = {
        "somekey":"somevalue"
    }
    return render(request,'login_and_registration/index.html', context) 