from django.db import models

from apps.projects.models import Project
from apps.accounts.models import ElementalUser

class Gallery(models.Model):
    name = models.CharField(max_length=25)


class ProjectToGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)

    def __unicode__(self):
        return '{0} is in {1}'.format(self.project.name, self.gallery.name)


class UserToGallery(models.Model):
    user = models.ForeignKey(ElementalUser, on_delete=models.CASCADE)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('member', 'Member'),
    )

    def __unicode__(self):
        return '{0} is a(n) {1} of {2}'.format(self.user.username, self.status, self.gallery.name)