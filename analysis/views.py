from rest_framework import generics, permissions
from resume.models import Resume
from .tasks import process_resume


class ResumeAnalysisView(generics.UpdateAPIView):
    queryset = Resume.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        resume = self.get_object()
        process_resume.delay(resume.id)
