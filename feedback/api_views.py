# feedback/api_views.py
import csv
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback

@api_view(['GET'])
def export_mtn_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mtn_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Comment', 'Date Submitted'])
    for fb in MTNFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.date_submitted])
    return response

@api_view(['GET'])
def export_orange_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orange_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Comment', 'Date Submitted'])
    for fb in OrangeFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.date_submitted])
    return response

@api_view(['GET'])
def export_camtel_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="camtel_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Comment', 'Date Submitted'])
    for fb in CamtelFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.date_submitted])
    return response

@api_view(['GET'])
def export_nexttel_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nexttel_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Comment', 'Date Submitted'])
    for fb in NexttelFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.date_submitted])
    return response
