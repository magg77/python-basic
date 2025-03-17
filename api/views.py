from rest_framework import generics
from  rest_framework import viewsets
from store.models import Project, Task
from .serializers import ProjectSerializer, TaskWithProjectSerializer, ProjectWithTaskAllSerializer, TaskSerializer



# logica encapsulada en clases, cuando heredan usamos el serializador para convertir los modelos



# api views generics

# get project
class ProjectApiList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = 

# create project
class ProjectApiCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer    

# search project
class ProjectApiRetrieve(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



# Create your viewSets here:
# query por id - delete - listar - actualizar - guardar

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskWithProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectWithTaskAllSerializer

# save
class TaskViewSetSave(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
