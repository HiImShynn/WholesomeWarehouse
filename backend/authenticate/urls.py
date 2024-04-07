from django.urls import path

from . import views

urlpatterns = [
    path('csrf/', views.get_csrf, name='auth-csrf'),
    path('login/', views.login_view, name='auth-login'),
    path('logout/', views.logout_view, name='auth-logout'),
    path('session/', views.SessionView.as_view(), name='auth-session'),
    path('whoami/', views.WhoAmIView.as_view(), name='auth-whoami'),
]
