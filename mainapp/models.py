from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # 📷 cover image
    file = models.FileField(upload_to='books/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





# tests/models.py

from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/',blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)

    # class Meta:
    #     verbose_name ="Profil"

    def __str__(self):
        return f"{self.user.username} profili "