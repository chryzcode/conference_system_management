from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#the user model
class User(AbstractUser):
    full_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email + ' ' + str(self.full_name)

#the conference model
class Conference(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=450)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


#the talk model
class Talk(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=450)
    description = models.TextField()
    speakers = models.ManyToManyField(User, related_name='speakers', blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    conference = models.CharField(max_length=450)
    date_time = models.DateTimeField()
    duration = models.CharField(max_length=150)

    def __str__(self):
        return self.title + ' ' + str(self.conference)


    
