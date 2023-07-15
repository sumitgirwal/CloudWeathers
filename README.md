# CloudWeathers
CloudWeathers is a basic weather forecast app that provides users with weather information for various locations. The app aims to give users quick and easy access to current weather conditions and forecasts.

![Screenshot 2023-07-15 185753](https://github.com/sumitgirwal/CloudWeathers/assets/64283478/0d940e89-6eea-4b7f-8bf9-341b9bf8bdd8)

Live Demo: https://youtu.be/TlxnYcFuMH0


#### Built with
- Python 
- Django Framework
- Htmx
- Bootstrap5

#### Installation & Setup
- Install virtual env
```bash
python -m pip install --user virtualenv
python -m venv venv
```
- Activate virtual env
```bash
.\venv\Scripts\activate
```
- Install packages
```bash
pip install -r requirements.txt
```

- Database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

- Run application
```bash
python manage.py runserver
```
- Hit url in browser 
```bash
http://127.0.0.1:8000/
```
