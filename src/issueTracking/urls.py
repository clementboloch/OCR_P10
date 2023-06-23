from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view(), name='project_list'),
    path('<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('<int:pk>/users/', views.UserList.as_view(), name='contributor_list'),
    path('<int:project_id>/users/<int:user_id>/', views.ContributorDelete.as_view(), name='contributor_delete'),
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
