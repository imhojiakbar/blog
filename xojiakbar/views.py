from msilib.schema import ListView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from xojiakbar.forms import UserRegisterModelFrom, UserLoginForm, PostCreateForm
from xojiakbar.models import Post


class HomePageView(View):
    def get(self, request):
        return render(request, 'xojiakbar/home.html')



class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterModelFrom()
        return render(request, "xojiakbar/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterModelFrom(data=request.POST)
        if form.is_valid():
            messages.success(request, "User registered successfully")
            form.save()
            return redirect('xojiakbar:login')
        else:
            return render(request, "xojiakbar/register.html", {"form":form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "xojiakbar/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "User logged in successfully")
                return redirect("xojiakbar:home-page")
            else:
                messages.error(request, "Username or password is wrong")
                return redirect("xojiakbar:login")
        else:
            return render(request, "xojiakbar/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        return render(request, "xojiakbar/logout.html")

    def post(self, request):
        logout(request)
        messages.info(request, "User logged out successfully")
        return redirect("xojiakbar:home-page")


class AboutView(View):
    def get(self, request):
        return render(request, "xojiakbar/about.html")


class HomeView(View):
    def get(self, request):
        return render(request, "xojiakbar/home.html")


class PostFormView(View):
    def get(self, request):
        return render(request, "xojiakbar/post_form.html")


class UserPostsView(View):
    def get(self, request):
        return render(request, "xojiakbar/user_posts.html")


class PostDetailView(View):
    def get(self, request):
        return render(request, "xojiakbar/post_detail.html")


class PostConfirmDeleteView(View):
    def get(self, request):
        return render(request, "xojiakbar/post_confirm_delete.html")


# class UserPostView(View):
#     def get(self, request):
#         return render(request, "xojiakbar/user_posts.html")


class UserPostsCreateView(CreateView):
    model = Post
    form = PostCreateForm
    fields = ['title', 'content', 'user']
    template_name = "xojiakbar/post_create.html"
    get_absolute_url = reverse_lazy('xojiakbar:post-form')