from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    ContactMessage,
    Experience,
    Project,
    Skill,
    Education,
    Resume,
    Profile
)


def home(request):

    profile = Profile.objects.first()
    experience = Experience.objects.all()
    project = Project.objects.all()
    skill = Skill.objects.all()
    education = Education.objects.all()
    resume = Resume.objects.all()

    homecontent = {
        "profile": profile,
        "experience": experience,
        "project": project,
        "skill": skill,
        "education": education,
        "resume": resume
    }

    return render(request, "index.html", {"homecontent" : homecontent})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'conatct.html')

def resume(request):
    return render(request,'resume.html')