from django.urls import path
from .views import RegisterView, ProfileView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
]