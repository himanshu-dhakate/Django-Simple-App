from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projects = [
    {
        "id": 1,
        "name": "Cancer Diagnosis using Machine Learning",
        "Languages": ["Python", "C++", "Java", "JavaScript"],
        "Additional_Libraries": ["matplotlib", "numpy", "pandas", "sklearn", "seaborn"],
        "Description": "Reducing the misclassification rate of cancer diagnosis using machine different ML models",
        "url": "https://www.github.com/username/project1"
    },
    {
        "id": 2,
        "name": "Steering Wheel angle simulation",
        "Languages": ["Python", "C++", "Java", "JavaScript"],
        "Additional_Libraries": ["matplotlib", "numpy", "pandas", "sklearn", "seaborn"],
        "Description": "Automatically calculating the steering wheel angle according to the angle of the road",
        "url": "https://www.github.com/username/project2"
    },
    {
        "id": 3,
        "name": "IIMH-Intention Identification",
        "Languages": ["Python", "C++", "Java", "JavaScript"],
        "Additional_Libraries": ["matplotlib", "numpy", "pandas", "sklearn", "seaborn"],
        "Description": "Finding the speech of a person is intentional or non-intentional",
        "url": "https://www.github.com/username/project3"
    }
]

def index(request):
    return HttpResponse(
        """<center><h1>Hello Himanshu<h1></center>
        <center> <h1>Welcome to the project section<h1></center>
            <center> <h2><a href = "/myapp/projects"> MyProjects </a> <h2></center>
            """
        )


def myProjects(request):
    return render(request, 'myapp/home.html', context = {"my_projects": projects})

def projectById(request, id):
    project_details = ''
    for prj in projects:
        if prj['id'] == id:
            project_details = prj

    return render(request, 'myapp/projects.html', context = {"project_details": project_details})
