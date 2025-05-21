from django.urls import path

from . import views
from .views import SessionDetail

urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    # Session views
path('sessions/', views.session_index, name='session-index'),
    path('sessions/create/', views.SessionCreate.as_view(), name='session-create'),
    path('sessions/<int:pk>/', SessionDetail.as_view(), name='session-detail'),
    path('sessions/<int:pk>/update/', views.SessionUpdate.as_view(), name='session-update'),
    path('sessions/<int:pk>/delete/', views.SessionDelete.as_view(), name='session-delete'),

    # Auth views
    path('accounts/signup/', views.signup, name='signup'),
]
