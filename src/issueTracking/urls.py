from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsList.as_view(), name='projects_list'),
]

# /signup/
# /login/
# /projects/
# /projects/
# /projects/{id}/
# /projects/{id}/
# /projects/{id}/
# /projects/{id}/users/
# /projects/{id}/users/
# /projects/{id}/users/{id}
# /projects/{id}/issues/
# /projects/{id}/issues/
# /projects/{id}/issues/{id}
# /projects/{id}/issues/{id}
# /projects/{id}/issues/{id}/comments/
# /projects/{id}/issues/{id}/comments/
# /projects/{id}/issues/{id}/comments/{id}
# /projects/{id}/issues/{id}/comments/{id}
# /projects/{id}/issues/{id}/comments/{id}
