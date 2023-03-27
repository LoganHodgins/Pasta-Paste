from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm

from .forms import PostForm, SignUpForm
from .models import Post


class UserPaste(View):
    def get(self, request):
        return render(request, 'user_paste/user_paste.html', {'postForm': PostForm, 'user': request.user.username})

    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.post_author = request.user
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
        context['post_count'] = len(Post.objects.all())
        return context

class Paste(DetailView):
    template_name = 'user_paste/paste.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'post_url_slug'


class ViewPaste(ListView):
    template_name = 'user_paste/view_pastes.html'
    model = Post
    ordering = ['-post_created_date']
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        posts = []
        if not self.request.user.is_anonymous:
            posts = Post.objects.filter(post_author=self.request.user)

        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anon'] = self.request.user.is_anonymous
        context['posts'] = []       

        if not context['anon']:
            paginator = Paginator(Post.objects.filter(post_author=self.request.user), 6)
            page = context['page_obj']
            print(page.has_next())
            posts = paginator.page(page.number).object_list

            context['first_pages'] = paginator.get_elided_page_range(number=page.number, on_each_side=2, on_ends=0)
            context['post_count'] = len(posts)
            context['posts'] = posts

        return context


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user_paste/signup.html'
    success_url = reverse_lazy("login")