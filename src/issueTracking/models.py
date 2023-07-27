from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = [
        ("BE", "Backe-end"),
        ("FE", "Front-end"),
        ("iOS", "iOS"),
        ("Andr", "Android"),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # permission
    # role

    class Meta:
        unique_together = ("user", "project")

    def __str__(self):
        return f"{self.user} - {self.project}"


class Issue(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    tag = [
        ("BUG", "Bug"),
        ("IMPROVEMENT", "Amélioration"),
        ("TASK", "Tâche"),
    ]
    priority = [
        ("LOW", "Faible"),
        ("MEDIUM", "Moyenne"),
        ("HIGH", "Élevée"),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = [
        ("TODO", "À faire"),
        ("IN_PROGRESS", "En cours"),
        ("DONE", "Terminé"),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignee", default=author
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.project} ({self.status})"


class Comment(models.Model):
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue} - {self.description[:20]}"
