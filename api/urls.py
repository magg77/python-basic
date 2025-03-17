from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import(ProjectApiList, ProjectApiCreate, ProjectApiRetrieve, TaskViewSet, ProjectViewSet, TaskViewSetSave)


router = DefaultRouter()
router.register("task", TaskViewSet, basename="task")
router.register("project-task", ProjectViewSet, basename="project")
router.register("task-save", TaskViewSetSave, basename="task-save")

urlpatterns = [
    path("project-list/", ProjectApiList.as_view(), name="project-list"),
    path("project-create", ProjectApiCreate.as_view(), name="project-create"),
    path("project-retrieve/<int:pk>", ProjectApiRetrieve.as_view(), name="project-retrive"),


]

urlpatterns += router.urls