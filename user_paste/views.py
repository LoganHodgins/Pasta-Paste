from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

import string
import random

from .forms import PostForm
from .models import User, Post


class UserPaste(View):
    def get(self, request):
        return render(request, 'user_paste/user_paste.html', {'PostForm': PostForm})

    def post(self, request):
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            anon_username = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            anon_user = User.objects.create(user_name=anon_username)
            post = post_form.save(commit=False)
            post.post_author = anon_user
            post.save()

            return HttpResponseRedirect(reverse('user-paste'))

        return render(request, 'user_paste/user_paste.html', {'PostForm': PostForm})

class StartingPageView(ListView):
    template_name = 'user_paste/index.html'
    model = Post
    ordering = ['-post_created_date']
    context_object_name = 'pastes'
