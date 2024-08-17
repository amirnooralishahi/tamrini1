from django.urls import path
from . import views
urlpatterns = [
path('add_education/', views.add_education, name='add_education'),
path('add_exprerience/', views.ExperienceCreateView.as_view(), name='add_exprerience'),
path('create_profile/', views.create_profile, name='create_profile'),
path('register', views.register, name='register'),
path('dashboard', views.dashboard, name='dashboard'),
path('logout/', views.logout, name='logout'),
path('login/', views.login, name='login'),
path('profile/<slug:slug>/update', views.UserProfileUpdateView.as_view(), name='create_profile'),
path('profile/<slug:slug>', views.ProfileDetailView.as_view(), name='profile_detail'),
path('profiles/', views.ProfileListView.as_view(), name='profiles'),

]








