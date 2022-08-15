from django.shortcuts import redirect
from django.urls import reverse

def handler(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return redirect('/login')