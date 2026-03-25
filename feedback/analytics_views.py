# feedback/analytics_views.py
from django.shortcuts import render
from django.db.models import Count
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback

def feedback_analytics(request):
    data = {
        'mtn_count': MTNFeedback.objects.count(),
        'orange_count': OrangeFeedback.objects.count(),
        'camtel_count': CamtelFeedback.objects.count(),
        'nexttel_count': NexttelFeedback.objects.count(),
    }
    return render(request, 'feedback_analytics.html', data)
