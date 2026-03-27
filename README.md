📡 NH-NETWORK — Nationwide Mobile Network Quality Monitoring System

A Django-powered system that collects, analyzes, and reports mobile network performance across Cameroon.

🚀 Overview

NH-NETWORK is a network quality monitoring platform built with HTML, CSS, JavaScript, Python, Django, and REST APIs.
It allows users across Cameroon to report:

Network signal quality
Connection speed
GPS location performance
Provider feedback (MTN, Orange, Camtel, Nexttel)
User experience ratings & complaints

The system aggregates all feedback into a central database and provides:

📊 Real-time analytics dashboards
🗂️ CSV export for telecom regulators
🔄 Auto & manual API forwarding to operators
🌍 Interactive maps (Leaflet.js)

This platform helps telecommunication companies and government agencies (ART Cameroon) improve mobile network quality nationwide.

✨ Key Features
🟡 For Users
Simple and responsive UI
Select your mobile provider
Submit feedback with location, speed & rating
Automatically detects wrong network provider
Works on mobile and desktop
🔵 For Administrators
Full Django Admin panel
CSV export for all 4 providers
Manual “Send to Provider” buttons
Midnight automated report sending
Performance analytics dashboard
IP lookup & geo-location support

🔧 Technical Features
Django REST API endpoints
WhiteNoise static files serving
SQLite (local) / PostgreSQL (production-ready)
Render deployment support
Modular provider-specific models
🏗️ Technology Stack
Layer	Technologies
Frontend	HTML, CSS, JavaScript
Backend	Python, Django, Django REST Framework
Database	SQLite (development), PostgreSQL (optional)
APIs	IPinfo API, Provider API endpoints
Deployment	Render Cloud Hosting
Tools	GitHub, Postman, Cron Jobs

📁 Project Structure
NH-NETWORK/
│── feedback/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── utils.py
│── nhnetwork/
│   ├── settings.py
│   ├── urls.py
│── staticfiles/ (collected)
│── db.sqlite3
│── requirements.txt
│── manage.py


🔌 API Endpoints
Provider Feedback Submission
Provider	Endpoint
MTN	POST /api/mtn/feedback/
Orange	POST /api/orange/feedback/
Camtel	POST /api/camtel/feedback/
Nexttel	POST /api/nexttel/feedback/
CSV Export Endpoints
Provider	Endpoint
MTN	/export/mtn/
Orange	/export/orange/
Camtel	/export/camtel/
Nexttel	/export/nexttel/


Admin Manual Trigger
/admin/feedback/mtnfeedback/send-to-mtn/
/admin/feedback/orangefeedback/send-to-orange/
/admin/feedback/camtelfeedback/send-to-camtel/
/admin/feedback/nexttelfeedback/send-to-nexttel/

📊 Analytics Dashboard

The admin analytics page provides:

Total feedback count
Provider-by-provider statistics
Most common ratings
Geographic mapping of poor coverage
Downloadable CSV insights





🛠️ Installation (Local Development)
1️⃣ Clone Repository
git clone https://github.com/dieudonne670/NH-NETWORK.git
cd NH-NETWORK
2️⃣ Create Virtual Environment
python3 -m venv env
source env/bin/activate  # Linux/Mac
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver
🚀 Deployment (Render)
Requirements
Add gunicorn to requirements.txt
Add staticfiles/ to repository
In Render → Web Service:

Build command:

pip install -r requirements.txt
python manage.py collectstatic --noinput

Start command:

gunicorn nhnetwork.wsgi
Environment Variables
Key	Value
DEBUG	False
SECRET_KEY	your-django-secret
IPINFO_TOKEN	your API token
🧪 Testing

Use Postman to test API endpoints:

POST /api/mtn/feedback/
{
  "name": "John",
  "email": "john@example.com",
  "rating": 3,
  "comment": "Slow network around Buea",
  "latitude": 4.156,
  "longitude": 9.231,
  "speed": 2.5
}


🔮 Future Improvements
Mobile App (Flutter or React Native)
AI-powered network prediction
Real-time provider dashboards
Integration with Cameroon ART
In-app map heat-zones
📝 License

This project is open-source and available under the MIT License.

👤 Author

Kindong Dieudonne
Backend Developer | Mobile Networks Enthusiast
GitHub: @dieudonne670
