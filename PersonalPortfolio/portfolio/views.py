from django.shortcuts import render
from .models import WorkExperience, Education, Skill
# Create your views here.
from django.shortcuts import render
from .models import Project

def home(request):
    context = {
        'name': 'Rohith',
        'photo_url': 'https://example.com/photo.jpg',
        'email': 'rohithmalae.com',
        'github_url': 'https://github.com/yourusername',
    }
    return render(request, 'home.html', context)


def portfolio(request):
    projects = Project.objects.all()
    work_experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()

    context = {
        'projects': projects,
        'work_experiences': work_experiences,
        'educations': educations,
        'skills': skills
    }
    
    return render(request, 'portfolio.html', context)


def about(request):
    context = {
        'bio': 'Write something about yourself here.',
        'skills': ['python', 'java',],
    }
    return render(request, 'about.html', context)




    

  