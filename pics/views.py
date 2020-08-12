from django.views.generic import (TemplateView, CreateView, ListView, UpdateView, DetailView, FormView)
from django.contrib.auth.models import User, auth

from pics.forms import UserCreationForm, UserInfoForm, PostForm, CommentForm, ChangeForm
from pics.models import Profile, Post, Comments
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404, reverse

from django.urls import reverse_lazy
from pics.forms import userForm


class SignUp(CreateView):
    form_class = userForm
    template_name = 'pics/signup.html'
    success_url = reverse_lazy('login')


class LoginPage(CreateView):
    template_name = 'pics/login_signup_page.html'
    success_url = reverse_lazy('login')


class UploadPage(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    model = Post
    form_class = PostForm
    template_name = 'pics/upload_form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(UploadPage, self).get_context_data(**kwargs)
        context['profilo'] = Profile.objects.all().order_by('-date')
        # Add any other variables to the context here
        ...
        return context


@login_required
def post_publish(request):
    Post.uploadPost()
    return redirect('home')


class ProfileDetail(DetailView):
    model = Profile


class ProfilePage(CreateView):
    login_url = '/login/'
    model = Profile
    form_class = UserInfoForm
    context_object_name = 'profilo'

    template_name = 'pics/user_form_page.html'
    success_url = reverse_lazy('pics:user')

    def form_valid(self, form):
        form.save(self.request.user)

        return super(ProfilePage, self).form_valid(form)

    @login_required
    def profile_publish(request):
        Profile.save_profile()
        return redirect('pics:user')

    def get_success_url(self, *args, **kwargs):
        return reverse("pics:user")


class changeP(UpdateView):
    login_url = '/login/'
    model = Profile
    form_class = ChangeForm
    template_name = 'pics/user_form_page.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super(changeP, self).form_valid(form)

    @login_required
    def profile_update(request):
        Profile.save_profile()
        return redirect('pics:user')

    def get_object(self, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return profile

    def get_success_url(self, *args, **kwargs):
        return reverse("pics:user")



class ProfilePageUpdate(UpdateView):
    login_url = '/login/'
    model = Profile
    form_class = UserInfoForm

    template_name = 'pics/user_form_page.html'

    def form_valid(self, form):
        form.save(self.request.user)

        return super(ProfilePageUpdate, self).form_valid(form)

    @login_required
    def profile_update(request):
        Profile.save_profile()
        return redirect('pics:user')

    def get_object(self, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return profile

    def get_success_url(self, *args, **kwargs):
        return reverse("pics:user")


class UserPage(ListView, LoginRequiredMixin):
    login_url = '/login/'
    queryset = Profile.objects.all()
    model = Profile
    context_object_name = 'profilo'
    template_name = 'pics/user.html'

    def get_context_data(self, **kwargs):
        context = super(UserPage, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date')

        return context

    def get_queryset(self):
        return Profile.objects.filter(date__lte=timezone.now()).order_by('-date')


class HomePage(ListView, LoginRequiredMixin):
    login_url = '/login/'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    model = Post
    template_name = 'pics/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['profilo'] = Profile.objects.all().order_by('-date')

        return context

    def get_queryset(self):
        return Post.objects.filter(date__lte=timezone.now()).order_by('-date')


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            comment.save()
            return redirect('home', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'pics/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    comment.approve()
    return redirect('home', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('home', pk=post_pk)
