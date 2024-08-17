from django.shortcuts import render
from django.shortcuts import  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import  messages
from django.views import View

from django.contrib.auth import  (authenticate,
                                  login as django_login,
                                  logout as django_logout)
from django.shortcuts import redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView
from .models import  UserProfile,Experience
from  .forms import UserProfileCreationForm
# Create your views here.
def add_education(request):
    return render(request, 'accounts/add-education.html')
def add_exprerience(request):
    return render(request, 'accounts/experience_form.html')
def create_profile(request):
    return render(request, 'accounts/create-profile.html')
@login_required()
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login(request):
        global form
        if request.method == "GET":
            form = AuthenticationForm()
        elif request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    django_login(request, user)
                    messages.add_message(request, messages.SUCCESS
                                         , f"wellcom{username}!")
                    return redirect(reverse('dashboard'))
                messages.add_message(request, messages.ERROR
                                     , f"user{username} was not found")
        return render(request, 'accounts/login.html', context={"form": form})


def logout(request):
    django_logout(request)
    return redirect(reverse('index'))

class UserProfileUpdateView(View,LoginRequiredMixin):
    def get(self,request,slug):
        user_profile = UserProfile.objects.get(slug=slug)
        form = UserProfileCreationForm(instance=user_profile)
        return  render(request,"accounts/create-profile.html",{'form':form})
    def post(self,request,slug):
        form = UserProfileCreationForm(data=request.POST,
                                       files= request.FILES,
                                       instance=request.user.userprofile)
        if form.is_valid():
            # user_profile =form.save(commit=False)
            # user_profile.user=request.user
            # user_profile.slug=request.user.userprofile.slug
            # user_profile.save()
            # user_profile = request.user.userprofile
            # user_profile.bio= form.cleaned_data['bio']
            # user_profile.picture=form.cleaned_data['picture']
            # user_profile.save()
            form.save()

            return redirect(reverse('dashboard'))
        return render(request,"accounts/create-profile.html",{'form':form})
# def profiles(request):
#     user_profiles=UserProfile.objects.all()
#     return render(request, 'accounts/userprofile_list.html'
#                   ,context={'user_profiles':user_profiles})
# def profile(request,slug):
#     user_profile =get_object_or_404(UserProfile,slug=slug,)
#     # user_profile=UserProfile.objects.get(id=id)
#     print(id)
#     return render(request, 'accounts/userprofile_detail.html'
#                   ,context={'user_profile':user_profile})
class ProfileDetailView(DetailView):
    model = UserProfile
    slug_url_kwarg = 'slug'

class ProfileListView(ListView):
    # template_name = 'accounts/userprofile_list.html'
    # queryset = UserProfile.objects.all()
    # context_object_name = 'profiles'
    model = UserProfile

class ExperienceCreateView(CreateView,LoginRequiredMixin):
    model = Experience

    fields = ['company','start_date','end_date','position','description']
    success_url = reverse_lazy("index")
    def form_valid(self, form):
        form.instance.userprofile=self.request.user.userprofile
        form.save()
        return super().form_valid(form)
def register(request):
    if request.method=="GET":
        form=UserCreationForm()
        return render(request, 'accounts/register.html'
                      ,context={'form':form})
    elif request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            # email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            User.objects.create_user(username,password1)
            messages.add_message(request,messages.SUCCESS,f"user{username} has been created")
            return redirect(reverse('login'))

        else:
                return render(request, 'accounts/register.html'
                              , context={'form': form})

