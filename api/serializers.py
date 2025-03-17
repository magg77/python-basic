from rest_framework import serializers
from store.models import Project

# serializador de modelo

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'