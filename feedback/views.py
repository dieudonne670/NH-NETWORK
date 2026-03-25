from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.http import HttpResponse
import csv


@csrf_exempt
def submit_feedback(request):
    
    if request.method == 'POST':
        data = request.POST
        feedback = Feedback.objects.create(
            provider=data.get('provider'),
            ip_address=data.get('ip_address'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            rating=data.get('rating'),
            comment=data.get('comment')
        )
        return JsonResponse({'status': 'success', 'message': 'Feedback saved'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


# Create your views here

def index_page(request):
    return render(request, 'feedback/index.html')  # Adjust the template path if needed

def mtn_page(request):
    return render(request, 'feedback/mtn.html')
def camtel_page(request):
    return render(request, 'feedback/camtel.html')
def orange_page(request):
    return render(request, 'feedback/orange.html')
def nexttel_page(request):
    return render(request, 'feedback/nexttel.html')
from django.shortcuts import render

def login_page(request):
    return render(request, 'feedback/login.html')  # Adjust path if needed
def signup_page(request):
    return render(request, 'feedback/signup.html')  # Adjust path if needed
def about_page(request):
    return render(request, 'feedback/about.html')
def networktype_page(request):
    return render(request, 'feedback/networktype.html') 


#for feedback analytics
# feedback/views.py
# feedback/views.py
# feedback/views.py
# feedback/views.py
from django.shortcuts import render

def feedback_analytics(request):
    total_feedback = Feedback.objects.count()

    # Count feedback per provider
    provider_counts = {
        'MTN': Feedback.objects.filter(provider='MTN').count(),
        'Orange': Feedback.objects.filter(provider='Orange').count(),
        'Camtel': Feedback.objects.filter(provider='Camtel').count(),
        'Nexttel': Feedback.objects.filter(provider='Nexttel').count(),
    }

    context = {
        'total_feedback': total_feedback,
        'provider_counts': provider_counts,
    }
    return render(request, 'feedback/feedback_analytics.html', context)


# Login view
# feedback/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return render(request, 'feedback/signup.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'feedback/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'feedback/signup.html')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'feedback/signup.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('networktype')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'feedback/login.html')

    return render(request, 'feedback/login.html')


@login_required
def network_type(request):
    return render(request, 'networktype.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


# feedback/views.py
# feedback/views.py

# at top of file (if not already)
  # ensure this import exists

# replace/define mtn_page
def mtn_page(request):
    """
    Handles GET to render the MTN page and POST to accept MTN feedback.
    Posts come from the mtn.html form (action="{% url 'mtn' %}").
    """
    if request.method == "POST":
        # read values (strings)
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        speed = request.POST.get('speed')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '').strip()

        # try to convert numeric values safely
        try:
            latitude = float(lat) if lat else None
        except (TypeError, ValueError):
            latitude = None

        try:
            longitude = float(lon) if lon else None
        except (TypeError, ValueError):
            longitude = None

        try:
            speed_val = float(speed) if speed else None
        except (TypeError, ValueError):
            speed_val = None

        try:
            rating_val = int(rating) if rating else None
        except (TypeError, ValueError):
            rating_val = None

        # Provide fallback name/email so model save won't fail (BaseFeedback requires them).
        # If you later add name/email inputs to the form, those will be used instead.
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', '')

        # Create record
        MTNFeedback.objects.create(
            name=name,
            email=email,
            comment=comment,
            latitude=latitude,
            longitude=longitude,
            speed=speed_val,
            rating=rating_val if rating_val is not None else 0,
        )

        # optional: add a success message and redirect to a success page or back to same page
        messages.success(request, "Thanks — your MTN feedback has been received.")
        # Redirect so refresh doesn't re-submit the form
        return redirect('mtn')

    # GET: render the page
    return render(request, 'feedback/mtn.html')







def orange_page(request):
    """
    Handles GET to render the MTN page and POST to accept MTN feedback.
    Posts come from the mtn.html form (action="{% url 'camtel' %}").
    """
    if request.method == "POST":
        # read values (strings)
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        speed = request.POST.get('speed')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '').strip()

        # try to convert numeric values safely
        try:
            latitude = float(lat) if lat else None
        except (TypeError, ValueError):
            latitude = None

        try:
            longitude = float(lon) if lon else None
        except (TypeError, ValueError):
            longitude = None

        try:
            speed_val = float(speed) if speed else None
        except (TypeError, ValueError):
            speed_val = None

        try:
            rating_val = int(rating) if rating else None
        except (TypeError, ValueError):
            rating_val = None

        # Provide fallback name/email so model save won't fail (BaseFeedback requires them).
        # If you later add name/email inputs to the form, those will be used instead.
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', '')

        # Create record
        OrangeFeedback.objects.create(
            name=name,
            email=email,
            comment=comment,
            latitude=latitude,
            longitude=longitude,
            speed=speed_val,
            rating=rating_val if rating_val is not None else 0,
        )

        # optional: add a success message and redirect to a success page or back to same page
        messages.success(request, "Thanks — your orange feedback has been received.")
        # Redirect so refresh doesn't re-submit the form
        return redirect('orange')


    # GET: render the page
    return render(request, 'feedback/orange.html')






def camtel_page(request):
    """
    Handles GET to render the MTN page and POST to accept MTN feedback.
    Posts come from the mtn.html form (action="{% url 'camtel' %}").
    """
    if request.method == "POST":
        # read values (strings)
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        speed = request.POST.get('speed')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '').strip()

        # try to convert numeric values safely
        try:
            latitude = float(lat) if lat else None
        except (TypeError, ValueError):
            latitude = None

        try:
            longitude = float(lon) if lon else None
        except (TypeError, ValueError):
            longitude = None

        try:
            speed_val = float(speed) if speed else None
        except (TypeError, ValueError):
            speed_val = None

        try:
            rating_val = int(rating) if rating else None
        except (TypeError, ValueError):
            rating_val = None

        # Provide fallback name/email so model save won't fail (BaseFeedback requires them).
        # If you later add name/email inputs to the form, those will be used instead.
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', '')

        # Create record
        CamtelFeedback.objects.create(
            name=name,
            email=email,
            comment=comment,
            latitude=latitude,
            longitude=longitude,
            speed=speed_val,
            rating=rating_val if rating_val is not None else 0,
        )

        # optional: add a success message and redirect to a success page or back to same page
        messages.success(request, "Thanks — your camtel feedback has been received.")
        # Redirect so refresh doesn't re-submit the form
        return redirect('camtel')


    # GET: render the page
    return render(request, 'feedback/camtel.html')



def nexttel_page(request):
    """
    Handles GET to render the MTN page and POST to accept MTN feedback.
    Posts come from the mtn.html form (action="{% url 'camtel' %}").
    """
    if request.method == "POST":
        # read values (strings)
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        speed = request.POST.get('speed')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '').strip()

        # try to convert numeric values safely
        try:
            latitude = float(lat) if lat else None
        except (TypeError, ValueError):
            latitude = None

        try:
            longitude = float(lon) if lon else None
        except (TypeError, ValueError):
            longitude = None

        try:
            speed_val = float(speed) if speed else None
        except (TypeError, ValueError):
            speed_val = None

        try:
            rating_val = int(rating) if rating else None
        except (TypeError, ValueError):
            rating_val = None

        # Provide fallback name/email so model save won't fail (BaseFeedback requires them).
        # If you later add name/email inputs to the form, those will be used instead.
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', '')

        # Create record
        NexttelFeedback.objects.create(
            name=name,
            email=email,
            comment=comment,
            latitude=latitude,
            longitude=longitude,
            speed=speed_val,
            rating=rating_val if rating_val is not None else 0,
        )

        # optional: add a success message and redirect to a success page or back to same page
        messages.success(request, "Thanks — your nexttel feedback has been received.")
        # Redirect so refresh doesn't re-submit the form
        return redirect('nexttel')


    # GET: render the page
    return render(request, 'feedback/nexttel.html')








@api_view(["POST"])
def dummy_provider(request):
    file = request.FILES.get("file")
    if file:
        return Response({"status": "received", "filename": file.name})
    return Response({"error": "no file"}, status=400)





@csrf_exempt
def mtn_feedback_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        feedback = MTNFeedback.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            comment=data.get("comment"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            speed=data.get("speed"),
            rating=data.get("rating"),
        )
        return JsonResponse({"message": "MTN feedback saved!", "id": feedback.id}, status=201)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

@csrf_exempt
def orange_feedback_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        feedback = OrangeFeedback.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            comment=data.get("comment"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            speed=data.get("speed"),
            rating=data.get("rating"),
        )
        return JsonResponse({"message": "ORANGE feedback saved!", "id": feedback.id}, status=201)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

@csrf_exempt
def camtel_feedback_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        feedback = CamtelFeedback.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            comment=data.get("comment"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            speed=data.get("speed"),
            rating=data.get("rating"),
        )
        return JsonResponse({"message": "CAMTEL feedback saved!", "id": feedback.id}, status=201)

    return JsonResponse({"error": "Only POST allowed"}, status=405)


@csrf_exempt
def nexttel_feedback_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        feedback = NexttelFeedback.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            comment=data.get("comment"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            speed=data.get("speed"),
            rating=data.get("rating"),
        )
        return JsonResponse({"message": "NEXTTEL feedback saved!", "id": feedback.id}, status=201)

    return JsonResponse({"error": "Only POST allowed"}, status=405)





def export_mtn_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mtn_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'email', 'comment', 'latitude', 'longitude', 'speed', 'rating', 'date_submitted'])
    for fb in MTNFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.latitude, fb.longitude, fb.speed, fb.rating, fb.date_submitted])
    return response


def export_orange_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orange_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'email', 'comment', 'latitude', 'longitude', 'speed', 'rating', 'date_submitted'])
    for fb in OrangeFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.latitude, fb.longitude, fb.speed, fb.rating, fb.date_submitted])
    return response


def export_camtel_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="camtel_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'email', 'comment', 'latitude', 'longitude', 'speed', 'rating', 'date_submitted'])
    for fb in CamtelFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.latitude, fb.longitude, fb.speed, fb.rating, fb.date_submitted])
    return response

def export_nexttel_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nexttel_feedback.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'email', 'comment', 'latitude', 'longitude', 'speed', 'rating', 'date_submitted'])
    for fb in NexttelFeedback.objects.all():
        writer.writerow([fb.name, fb.email, fb.comment, fb.latitude, fb.longitude, fb.speed, fb.rating, fb.date_submitted])
    return response