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
    skill = Skill.objects.all()
    return render(request,'about.html',{
        "skills" : skill 
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = request.POST.get('contact')

        ContactMessage.objects.create(
            name=name,
            email=email,
            contact=contact,
            subject=subject,
            message=message
        )
    return render(request,'conatct.html')

def resume(request):
    resume = Resume.objects.first()
    return render(request,'resume.html',{
        "resume" : resume
    })