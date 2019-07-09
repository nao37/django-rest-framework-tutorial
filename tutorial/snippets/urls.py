from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet_list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
