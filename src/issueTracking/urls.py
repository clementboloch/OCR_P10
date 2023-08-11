from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view(), name='project_list'),
    path('<int:project_id>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('<int:project_id>/users/', views.ContributorList.as_view(), name='contributor_list'),
    path('<int:project_id>/users/<int:user_id>/', views.ContributorDelete.as_view(), name='contributor_delete'),
    path('<int:project_id>/issues/', views.IssueList.as_view(), name='issue_list'),
    path('<int:project_id>/issues/<int:issue_id>/', views.IssueUpdate.as_view(), name='issue_update'),
    path('<int:project_id>/issues/<int:issue_id>/comments/', views.CommentList.as_view(), name='comment_list'),
    path('<int:project_id>/issues/<int:issue_id>/comments/<comment_id>/', views.CommentUpdate.as_view(), name='comment_update'),
]
