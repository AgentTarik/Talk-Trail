from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, TemplateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import UserProfile, Post
from .forms import UserRegisterForm, PostForm, UserProfileForm, UserDeleteForm
from django.contrib.auth.forms import AuthenticationForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class UserRegisterView(CreateView):
    model = UserProfile
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

class UserLoginView(DjangoLoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('feed')


    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            auth_login(self.request, user)
            return super().form_valid(form)
        else:
            # This handles the case where authentication fails
            form.add_error(None, "Please enter a correct username and password.")
            return self.form_invalid(form)


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile_edit')

    def get_object(self):
        return self.request.user


class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'profile_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        self.get_object().posts.all().delete()
        return super().delete(request, *args, **kwargs)


class FeedView(LoginRequiredMixin, FormView):
    template_name = 'feed.html'
    form_class = PostForm
    success_url = '/feed/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[::-1]
        context['user'] = self.request.user
        return context