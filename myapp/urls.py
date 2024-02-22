from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="my_name"),
    path('projects/', views.myProjects, name="projects_name"),
    path('projectByID/<int:id>/', views.projectById, name="projectGetFromId")
]
