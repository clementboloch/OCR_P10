from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.Contributor)
admin.site.register(models.Issue)
admin.site.register(models.Comment)
