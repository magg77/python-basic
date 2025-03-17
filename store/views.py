from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Project, Task

# Create your views here.

def ProjectTaskXml(request):
    projects = Project.objects.all()
    projects_serializer = serialize("xml", projects)
    return HttpResponse(projects_serializer, content_type="text/xml")

def ProjectTaskJson(request):
    projects = Project.objects.all()
    projects_serializer = serialize("json", projects)
    return HttpResponse(projects_serializer, content_type="text/json")