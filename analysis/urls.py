from django.urls import path
from .views import ResumeAnalysisView

urlpatterns = [
    path('process/<int:pk>/', ResumeAnalysisView.as_view(), name='process_resume'),
]