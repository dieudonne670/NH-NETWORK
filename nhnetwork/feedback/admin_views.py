# feedback/admin_views.py
# feedback/admin_views.py
from django.shortcuts import render
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback

def feedback_analytics_view(request):
    counts = {
        'MTN': MTNFeedback.objects.count(),
        'Orange': OrangeFeedback.objects.count(),
        'Camtel': CamtelFeedback.objects.count(),
        'Nexttel': NexttelFeedback.objects.count(),
    }

    recent = {
        'MTN': MTNFeedback.objects.order_by('-submitted_at')[:10],
        'Orange': OrangeFeedback.objects.order_by('-submitted_at')[:10],
        'Camtel': CamtelFeedback.objects.order_by('-submitted_at')[:10],
        'Nexttel': NexttelFeedback.objects.order_by('-submitted_at')[:10],
    }

    return render(request, 'feedback/admin_analytics.html', {'counts': counts, 'recent': recent})
