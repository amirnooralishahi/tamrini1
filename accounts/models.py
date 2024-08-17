from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200,null=True)
    slug = models.SlugField(blank=True)
    bio = models.TextField(null=True)
    picture = models.ImageField(upload_to='profile_picture',null=True)

    def __str__(self):
        return  f"UserProfile({self.user.first_name}-{self.user.last_name})"
    def get_absolute_url(self):
            return reverse(
                'profile_detail',kwargs={'slug':self.slug}
            )
    def get_full_name(self):
        return f"{self.user.first_name}-{self.user.last_name}"

class Experience(models.Model):
    userprofile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    company= models.CharField(max_length=200)
    start_date=models.DateField()
    end_date=models.DateField(null=True)
    position=models.CharField(max_length=200)
    description=models.TextField(null=True)
    def __str__(self):
        return f"experience(user={self.userprofile.user.username})"

class Education(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    university=models.CharField(max_length=200)
    start_date=models.DateField()
    end_date=models.DateField(null=True)
    Degree=models.CharField(max_length=200)
    field_of_study=models.CharField(max_length=200)
    description=models.TextField(null=True)
    def __str__(self):
        return f"Education({self.university})"