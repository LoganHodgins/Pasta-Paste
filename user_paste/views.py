from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

import string
import random

from .forms import PostForm
from .models import User, Post


class UserPaste(View):
    def get(self, request):
        return render(request, 'user_paste/user_paste.html', {'postForm': PostForm})

    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            anon_username = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            anon_user = User.objects.create(user_name=anon_username)
            post = post_form.save(commit=False)
            post.post_author = anon_user
            post.save()

            return HttpResponseRedirect(reverse('index'))

        return render(request, 'user_paste/user_paste.html', {'postForm': PostForm})

class StartingPageView(ListView):
    template_name = 'user_paste/index.html'
    model = Post
    ordering = ['-post_created_date']
    context_object_name = 'pastes'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(Post.objects.all(), 6)
        page = context['page_obj']
        context['first_pages'] = paginator.get_elided_page_range(number=page.number, on_each_side=2, on_ends=0)
        return context

class Paste(DetailView):
    template_name = 'user_paste/paste.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'post_url_slug'

class Login(View):
    def get(self, request):
        return render(request, 'user_paste/login.html')