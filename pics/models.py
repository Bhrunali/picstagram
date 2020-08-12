from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User, auth

from django.utils import timezone


# from django.db.models.signals import post_save
# from django.dispatch import receiver
class user(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return f"@{self.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=350)
    profile_pic = models.ImageField(upload_to='ProfilePicture/', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_profile(self):
        self.save()

    def get_absolute_url(self):
        return reverse("pics:user", kwargs={'pk': self.pk})


def __str__(self):
    return self.profile.user


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    image_caption = models.CharField(max_length=700)
    tag_someone = models.CharField(max_length=50, blank=True)
    imageUploader_profile = models.ForeignKey(User, on_delete=models.CASCADE, null='True', blank=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def uploadPost(self):
        self.date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("pics/home", kwargs={'pk': self.pk})

    def __str__(self):
        return self.image_caption


class Comments(models.Model):
    comment_post = models.CharField(max_length=150)
    author = models.ForeignKey('Profile', related_name='commenter', on_delete=models.CASCADE)
    commented_image = models.ForeignKey('pics.Post', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.author
