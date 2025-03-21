from celery import shared_task
from resume.models import Resume


@shared_task()
def process_resume(resume_id):
    resume = Resume.objects.get(id=resume_id)

    # AI processing logic here
    resume.parsed_data = {"example": "data"}
    resume.save()
