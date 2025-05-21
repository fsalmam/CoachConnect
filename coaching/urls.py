from django.urls import path

from . import views
from .views import ApplicationDeleteView, ApplicationListView, SessionDetail

urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    # Coach session management
    path('sessions/', views.session_index, name='session-index'),
    path('sessions/create/', views.SessionCreate.as_view(), name='session-create'),
    path('sessions/<int:pk>/', SessionDetail.as_view(), name='session-detail'),
    path('sessions/<int:pk>/update/', views.SessionUpdate.as_view(), name='session-update'),
    path('sessions/<int:pk>/delete/', views.SessionDelete.as_view(), name='session-delete'),

    # Client session browsing & reservations
    path('sessions/available/', views.AvailableSessions.as_view(), name='available-sessions'),
    path('my-reservations/', ApplicationListView.as_view(), name='my-reservations'),
    path('reservations/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='reservation-delete'),

    # Authentication
    path('accounts/signup/', views.signup, name='signup'),
]
