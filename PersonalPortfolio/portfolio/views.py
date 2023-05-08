from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Project
from .models import WorkExperience, Education, Skill
from .forms import Project_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    context = {
        'name': 'Rohith',
        'photo_url': 'https://example.com/photo.jpg',
        'email': 'rohithmalae.com',
        'github_url': 'https://github.com/yourusername',
    }
    return render(request, 'home.html', context)

@login_required
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

@login_required
def about(request):
    context = {
        'bio': 'Write something about yourself here.',
        'skills': ['python', 'java',],
    }
    return render(request, 'about.html', context)


def form_view(request):
    form = Project_model()
    if request.method == 'POST':
        form = Project_model(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            year = request.POST.get('year')
            Project.objects.create(title = title, description = description, year = year)
            return render(request, 'portfolio/portfolio.html',{})
    context= {
        'form' : form
    }
    return render(request, 'portfolio/form.html', context)


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
   'form' : form
       }
    return render(request, 'portfolio/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': 'Invalid Username or Password'
            }

            return render(request, 'portfolio/login.html', context)
        login(request, user)
        return redirect('home') 
    context = {}
    return render(request, 'portfolio/login.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'portfolio/logout.html', {})




    

  