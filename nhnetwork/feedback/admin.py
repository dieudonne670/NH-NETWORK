# feedback/admin.py
from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback
from . import utils
import csv

# -----------------------
# Reusable CSV export
# -----------------------
def export_as_csv_action(description="Export Selected as CSV", fields=None):
    def export_as_csv(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="feedback.csv"'
        writer = csv.writer(response)
        writer.writerow(fields)
        for obj in queryset:
            row = [getattr(obj, field) for field in fields]
            writer.writerow(row)
        return response
    export_as_csv.short_description = description
    return export_as_csv

# -----------------------
# Main Feedback model
# -----------------------


search_fields = ('provider', 'ip_address', 'comment')
list_filter = ('provider', 'rating')
actions = [export_as_csv_action(fields=[
        'provider', 'rating', 'comment', 'ip_address',
        'latitude', 'longitude', 'submitted_at'
    ])]

# -----------------------
# Base provider feedback admin
# -----------------------
class ProviderFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'latitude', 'longitude', 'speed', 'rating', 'date_submitted')
    search_fields = ('name', 'email', 'comment')
    list_filter = ('rating',)
    actions = [export_as_csv_action(fields=[
        'name', 'email', 'comment', 'latitude', 'longitude', 'speed', 'rating', 'date_submitted'
    ])]

# -----------------------
# MTN
# -----------------------
@admin.register(MTNFeedback)
class MTNFeedbackAdmin(ProviderFeedbackAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("send-to-mtn/", self.admin_site.admin_view(self.send_to_mtn))
        ]
        return custom_urls + urls

    def send_to_mtn(self, request):
        status, msg = utils.send_mtn_feedback()
        if status == 200:
            self.message_user(request, "MTN feedback sent successfully!", level=messages.SUCCESS)
        else:
            self.message_user(request, f"Failed to send MTN feedback: {msg}", level=messages.ERROR)
        return HttpResponseRedirect("../")

# -----------------------
# Orange
# -----------------------
@admin.register(OrangeFeedback)
class OrangeFeedbackAdmin(ProviderFeedbackAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("send-to-orange/", self.admin_site.admin_view(self.send_to_orange))
        ]
        return custom_urls + urls

    def send_to_orange(self, request):
        status, msg = utils.send_orange_feedback()
        if status == 200:
            self.message_user(request, "Orange feedback sent successfully!", level=messages.SUCCESS)
        else:
            self.message_user(request, f"Failed to send Orange feedback: {msg}", level=messages.ERROR)
        return HttpResponseRedirect("../")

# -----------------------
# Camtel
# -----------------------
@admin.register(CamtelFeedback)
class CamtelFeedbackAdmin(ProviderFeedbackAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("send-to-camtel/", self.admin_site.admin_view(self.send_to_camtel))
        ]
        return custom_urls + urls

    def send_to_camtel(self, request):
        status, msg = utils.send_camtel_feedback()
        if status == 200:
            self.message_user(request, "Camtel feedback sent successfully!", level=messages.SUCCESS)
        else:
            self.message_user(request, f"Failed to send Camtel feedback: {msg}", level=messages.ERROR)
        return HttpResponseRedirect("../")

# -----------------------
# Nexttel
# -----------------------
@admin.register(NexttelFeedback)
class NexttelFeedbackAdmin(ProviderFeedbackAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("send-to-nexttel/", self.admin_site.admin_view(self.send_to_nexttel))
        ]
        return custom_urls + urls

    def send_to_nexttel(self, request):
        status, msg = utils.send_nexttel_feedback()
        if status == 200:
            self.message_user(request, "Nexttel feedback sent successfully!", level=messages.SUCCESS)
        else:
            self.message_user(request, f"Failed to send Nexttel feedback: {msg}", level=messages.ERROR)
        return HttpResponseRedirect("../")
