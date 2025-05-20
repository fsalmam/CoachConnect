from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sessions/', views.session_index, name='session-index'),
    path('sessions/<int:session_id>/', views.session_detail, name='session-detail'),
    path('sessions/create/', views.SessionCreate.as_view(), name='session-create'),
    path('sessions/<int:pk>/update/', views.SessionUpdate.as_view(), name='session-update'),
    path('sessions/<int:pk>/delete/', views.SessionDelete.as_view(), name='session-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
