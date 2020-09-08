from django.urls import include, path

from .views import ProjectDetail, UserDetail, ProjectCreate

urlpatterns = [
    # nothing
    path('users/user/<pk>/', UserDetail.as_view(), name='user-data'),
    path('projects/project/<pk>/', ProjectDetail.as_view(), name='project-data'),
    path('projects/project/', ProjectCreate.as_view(), name='project-create'),
]