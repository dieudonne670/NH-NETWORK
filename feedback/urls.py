# feedback/urls.py

from django.urls import path
from . import views, api_views
from .admin_views import feedback_analytics_view

urlpatterns = [
    # General pages
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('networktype/', views.networktype_page, name='networktype'),

    # Network provider pages (HTML forms)
    path('mtn/', views.mtn_page, name='mtn'),
    path('orange/', views.orange_page, name='orange'),
    path('camtel/', views.camtel_page, name='camtel'),
    path('nexttel/', views.nexttel_page, name='nexttel'),

    # Feedback submission (general)
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),

    # Feedback analytics for users
    path('analytics/', views.feedback_analytics, name='user_feedback_analytics'),
    # feedback/urls.py


    # Feedback analytics for admin
    path('admin/feedback/analytics/', feedback_analytics_view, name='admin_feedback_analytics'),

    # ========================
    # 🚀 API Endpoints (JSON, for Postman)
    # ========================
    path("api/mtn/feedback/", views.mtn_feedback_api, name="mtn-feedback"),
    path("api/orange/feedback/", views.orange_feedback_api, name="orange-feedback"),
    path("api/camtel/feedback/", views.camtel_feedback_api, name="camtel-feedback"),
    path("api/nexttel/feedback/", views.nexttel_feedback_api, name="nexttel-feedback"),

    # ========================
    # 📂 CSV Export Endpoints
    # ========================
    path("api/export/mtn/", api_views.export_mtn_csv, name="export-mtn"),
    path("api/export/orange/", api_views.export_orange_csv, name="export-orange"),
    path("api/export/camtel/", api_views.export_camtel_csv, name="export-camtel"),
    path("api/export/nexttel/", api_views.export_nexttel_csv, name="export-nexttel"),

    # Dummy route (optional, only if needed for testing)
    path("dummy/upload/", views.dummy_provider, name="dummy_provider"),
]
