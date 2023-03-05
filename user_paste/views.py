from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def index(req):
    return render(req, 'user_paste/index.html')
