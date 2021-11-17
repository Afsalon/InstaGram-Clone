from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user
# Create your models here.
User= get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='p', on_delete=models.CASCADE, editable=False)
    post = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=100, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    class Meta:
        ordering=['-posted_on']
    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Post, self).save(*args, **kwargs)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    post = models.ForeignKey(Post, related_name='lik', on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.liked_on)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Like, self).save(*args, **kwargs)

class Comment(models.Model):
    text = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='postcomm',on_delete=models.CASCADE,editable=False)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Comment, self).save(*args, **kwargs)

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follow', on_delete=models.CASCADE,editable=False)
    follow = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "done"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Follow, self).save(*args, **kwargs)
