# 🌤️ Cameroon Weather App  
A modern, clean Django-based web application that shows real-time weather data for any city in Cameroon using the OpenWeather API.

---

## 🚀 Live Demo  
🟢 **COMING SOON** (hosted on Render)  
Once deployed, your live link will appear here.

---

## 📌 Features  
- ✔ Search weather by city (Cameroon)  
- ✔ Real-time temperature, humidity, wind speed  
- ✔ Beautiful Bootstrap UI  
- ✔ Uses secure environment variables (no API keys in source code)  
- ✔ Ready for production deployment (Render / Railway / Heroku)

---

## 🏗️ Project Structure  

cameroon-weather-app/
│
├── the_weather/
│   ├── the_weather/        # Django project settings
│   ├── weather/            # App code
│   ├── manage.py
│
├── static/weather/style.css
├── templates/weather/weather.html
├── requirements.txt
├── README.md
└── .gitignore

🔧 Local Installation
1. Clone the repository
git clone https://github.com/dieudonne670/cameroon-weather-app.git
cd cameroon-weather-app


2.create a virtualenvironment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add your environment variables

Create a file named .env in the project root:

5. Run the app
python manage.py runserver

Open:
👉 http://127.0.0.1:8000/

⚙️ Environment Variables
Variable	Description
OPENWEATHER_API_KEY	Your OpenWeather API key
SECRET_KEY	Django secret key
DEBUG	True/False
🚀 Deploying to Render

Build command

pip install -r requirements.txt

Start command

gunicorn the_weather.wsgi

Required environment variables

OPENWEATHER_API_KEY

SECRET_KEY

DEBUG=False

🧰 Technologies Used

Python 3

Django

Bootstrap 5

OpenWeather API

Gunicorn

👤 Author

Kindong Dieudonné
Limbe, Cameroon

OPENWEATHER_API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=django-secret-key-here


