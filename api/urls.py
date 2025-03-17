from django.urls import path
from .views import(ProjectApiList, ProjectApiCreate)

urlpatterns = [
    path("project-list/", ProjectApiList.as_view(), name="project-list"),
    path("project-create", ProjectApiCreate.as_view(), name="project-create"),
    
]