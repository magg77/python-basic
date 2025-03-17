from rest_framework import generics
from store.models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectApiList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = 

class ProjectApiCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer    


