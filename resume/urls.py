from django.urls import path, include
from .views import ResumeUploadView, ResumeDetailView

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
]