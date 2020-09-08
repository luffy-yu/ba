from django.urls import include, path
from django.contrib import admin

admin.autodiscover()

from .views import ProfileView, UserSettings, SignUp, Logout, Login

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('settings/', UserSettings.as_view(), name='user-settings'),
    path('register/', SignUp.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name="login"),
]
