from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='media/profile_images/')
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    # available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/project_images/')
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Resume(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='media/pdf')

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    contact = models.CharField(max_length=20)