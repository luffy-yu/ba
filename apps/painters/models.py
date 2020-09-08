from django.db import models

# Create your models here.
from apps.accounts.models import ElementalUser


class Painter(models.Model):
    name = models.CharField('name', max_length=50)
    user = models.ForeignKey(ElementalUser, on_delete=models.CASCADE)
    project = models.FilePathField()
    video = models.FilePathField()
    canvas = models.TextField()
    deleted = models.BooleanField(default=False)
    thumbnail = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(name='created', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'user')

    @staticmethod
    def get_all(request):
        projects = Painter.objects.all().filter(user=request.user).order_by(Painter.created.field.name)
        return projects
