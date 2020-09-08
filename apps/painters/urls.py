from django.urls import include, path

from .views import PainterCreate, CreateProject, UploadFile

urlpatterns = [
    path('painter/', PainterCreate.as_view(), name='create-painter'),
    path('upload/', UploadFile.as_view(), name='upload-file'),
    path('create/', CreateProject.as_view(), name='create'),
]
