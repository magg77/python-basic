from rest_framework import serializers
from store.models import Project, Task

# serializador de modelo
# convetir modelos de datos relacionados en serializables y se pueden enviar utilizando un responsehttp

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'





# serializador con viewSet

# get task con su respectivo project
class TaskWithProjectSerializer(serializers.ModelSerializer):
    #project = serializers.StringRelatedField(many=True)
    #project = serializers.StringRelatedField()
    #project = serializers.PrimaryKeyRelatedField(read_only=True)
    project = ProjectSerializer()
    
    class Meta:
        model = Task
        fields = '__all__'

# get all tasks de un project
class ProjectWithTaskAllSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'


