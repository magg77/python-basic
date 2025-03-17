from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=250)

    # devolver una representación en cadena de un objeto: panel de administración de Django
    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", null=False)

    # devolver una representación en cadena de un objeto: panel de administración de Django
    def __str__(self):
        return self.title
    