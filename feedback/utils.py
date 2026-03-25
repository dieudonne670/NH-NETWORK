import requests
import csv
from django.core.files.temp import NamedTemporaryFile
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback

def send_feedback_to_api(queryset, url, token):
    """Generate a CSV from queryset and send to provider API"""
    with NamedTemporaryFile(mode="w+", newline='', suffix=".csv") as tmpfile:
        writer = csv.writer(tmpfile)
        writer.writerow(['Name', 'Email', 'Comment', 'Date Submitted'])

        for fb in queryset:
            writer.writerow([fb.name, fb.email, fb.comment, fb.date_submitted])
        tmpfile.flush()

        headers = {"Authorization": f"Bearer {token}"}
        files = {"file": open(tmpfile.name, "rb")}

        response = requests.post(url, headers=headers, files=files)
        return response.status_code, response.text


def send_mtn_feedback():
    return send_feedback_to_api(
        MTNFeedback.objects.all(),
        "https://api.mtn.cm/feedback/upload",
        "YOUR_MTN_API_TOKEN"
    )

def send_orange_feedback():
    return send_feedback_to_api(
        OrangeFeedback.objects.all(),
        "https://api.orange.cm/feedback/upload",
        "YOUR_ORANGE_API_TOKEN"
    )

def send_camtel_feedback():
    return send_feedback_to_api(
        CamtelFeedback.objects.all(),
        "https://api.camtel.cm/feedback/upload",
        "YOUR_CAMTEL_API_TOKEN"
    )

def send_nexttel_feedback():
    return send_feedback_to_api(
        NexttelFeedback.objects.all(),
        "https://api.nexttel.cm/feedback/upload",
        "YOUR_NEXTTEL_API_TOKEN"
    )
