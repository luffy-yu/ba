from django.urls import include, path
from django.views.generic import TemplateView

from .views import ProjectCreate, ProjectEdit, MyProjects

urlpatterns = [
    path('editor/', ProjectCreate.as_view(), name='create-project'),
    path('project/<pk>', ProjectEdit.as_view(), name='edit-project'),
    path('mystuff/', MyProjects.as_view(), name='my-projects'),
    # url(r'^(?i)proof-of-concept/', TemplateView.as_view(template_name='proof-of-concept.html')),
]