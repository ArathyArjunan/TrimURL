# **ShortyAPI – Django URL Shortener**

A full-stack URL shortener built with **Django REST Framework** for the backend
Features include:

- User registration & login (JWT authentication)  
- Shorten URLs with unique short codes  
- Track clicks for each short link  
- View, refresh, and delete your own links  
- Redirect short URLs to the original website  

---

## **Features**
✅ User Authentication (Register, Login with JWT)  
✅ Create short URLs  
✅ View your list of URLs with click counts  
✅ Redirect short URLs to their original destination  
✅ Delete URLs you no longer need  
✅ Responsive minimal frontend UI  

---

## **Tech Stack**
- **Backend:** Python, Django, Django REST Framework, SimpleJWT  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (can be replaced with PostgreSQL/MySQL)  

---

## **Project Structure**
shorturl/
│
├── api
│ ├── migrations/
│ ├── templates/
│ │ └── index.html # Frontend UI
│ ├── models.py # Link model
│ ├── serializers.py # DRF serializers
│ ├── views.py # API endpoints
│ ├── url_generator.py # Random short code generator
│ ├── urls.py # App-level routes
│
├── shorturl/
│ ├── settings.py # Django settings
│ ├── urls.py # Project-level routes
│
├── manage.py
└── README.md


---

## **Installation & Setup**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ArathyArjunan/TrimURL
cd shorturl

2️⃣ Create Virtual Environment
python -m venv venv 
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

3 Create .env
SECRET_KEY=""
DEBUG=False
DATABASE_URL=""
ALLOWED_HOSTS=*


Example requirements.txt:

Django>=5.0
djangorestframework
djangorestframework-simplejwt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (Optional)
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver


The app will run at: http://127.0.0.1:8000/

Open http://127.0.0.1:8000/

Register a new account or login.

Enter a URL and click Shorten.

Copy the generated short link.

Share it — anyone can use it to be redirected.

Manage your links in the dashboard (view clicks, delete links).
