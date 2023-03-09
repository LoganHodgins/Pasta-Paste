from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

from .forms import PostForm

def index(req):
    return render(req, 'user_paste/index.html', {'PostForm': PostForm})