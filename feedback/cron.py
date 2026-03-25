from .utils import send_mtn_feedback, send_orange_feedback, send_camtel_feedback, send_nexttel_feedback
import requests
import tempfile
import csv
from django.utils.timezone import now
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback

def send_all_feedbacks():
    send_mtn_feedback()
    send_orange_feedback()
    send_camtel_feedback()
    send_nexttel_feedback()



PROVIDER_APIS = {
    "MTN": "https://api.mtn.cm/feedback/upload/",
    "Orange": "https://api.orange.cm/feedback/upload/",
    "Camtel": "https://api.camtel.cm/feedback/upload/",
    "Nexttel": "https://api.nexttel.cm/feedback/upload/"
}

def export_and_send(provider, queryset):
    # Create temp CSV file
    with tempfile.NamedTemporaryFile(mode="w+", newline="", suffix=".csv") as tmpfile:
        writer = csv.writer(tmpfile)
        writer.writerow(["name", "email", "comment", "date", "lat", "lon", "speed", "rating"])

        for fb in queryset:
            writer.writerow([
                fb.name, fb.email, fb.comment, fb.date_submitted,
                getattr(fb, "latitude", ""), getattr(fb, "longitude", ""),
                getattr(fb, "speed", ""), getattr(fb, "rating", "")
            ])
        tmpfile.flush()

        # Send CSV to provider API
        files = {"file": open(tmpfile.name, "rb")}
        url = PROVIDER_APIS[provider]
        response = requests.post(url, files=files)

        if response.status_code == 200:
            print(f"✅ {provider} CSV sent successfully")
        else:
            print(f"❌ {provider} failed: {response.status_code} {response.text}")


def send_all_feedbacks():
    export_and_send("MTN", MTNFeedback.objects.all())
    export_and_send("Orange", OrangeFeedback.objects.all())
    export_and_send("Camtel", CamtelFeedback.objects.all())
    export_and_send("Nexttel", NexttelFeedback.objects.all())
