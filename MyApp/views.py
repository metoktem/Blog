from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterFormWithNames
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')  # veya başka bir sayfaya yönlendirin
    else:
        form = PostForm()
    return render(request, 'MyApp/create_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # veya başka bir sayfaya yönlendirin
    else:
        form = PostForm(instance=post)
    return render(request, 'MyApp/update_post.html', {'form': form})


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(is_deleted=False)

def home_view_general(request):
    return render(request, 'MyApp/home.html')

def home_view_profile(request):
    return render(request, 'MyApp/profile.html')

def login_view(request):
    return render(request, 'MyApp/login.html')

def register_view(request):
    return render(request, 'MyApp/register.html')

def postlist_view(request):
    return render(request, 'MyApp/post_list.html')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')  # Silme işlemi tamamlandığında yönlendirilecek sayfa
    template_name = 'post_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        # Silme işlemi yerine is_deleted alanını güncelleyerek işaretleme
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')  # Yeni kayıt işlemi tamamlandığında yönlendirilecek sayfa
    else:
        form = UserCreationForm()
    return render(request, 'MyApp/register.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterFormWithNames(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Tebrikler, Kullanıcı başarıyla oluşturuldu. ')
            return redirect('post_list')
    else:
        form = RegisterFormWithNames()
    return render(request, 'MyApp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')  # veya başka bir sayfaya yönlendirin
    else:
        form = LoginForm()
    return render(request, 'MyApp/login.html', {'form': form})


def post_list(request):
    post_list = Post.objects.filter(author=request.user)
    return render(request, 'MyApp/post_list.html', {'post_list': post_list})


def home_view(request):
    post_list = Post.objects.all()
    return render(request, 'MyApp/home.html', {'post_list': post_list})


