from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    ROLE_CHOICES = (
        ('coach', 'Coach'),
        ('client', 'Client'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f'{self.user.username} - {self.role}'


class Session(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)  # The coach who created the session

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('session-detail', kwargs={'pk': self.pk})


class Application(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.applicant.username} → {self.session.title}'
