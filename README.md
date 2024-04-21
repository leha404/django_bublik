# django_bublik

## Pet project for photographers sales point

**Inspired by DjangoGirls:** 

https://tutorial.djangogirls.org/ru/django/

---

### Install Instructions:
1. Install virtual env (macOS):  
`python3 -m venv myvenv`

2. Run virtual environment:  
`source myvenv/bin/activate`

3. Update Python package manager:  
`python3 -m pip install --upgrade pip`

4. Get requirement packages (check requirements.txt):  
`pip install -r requirements.txt`

- *In requirements:*  
`Django~=3.2.10`

5. _*optional:_ Get Django default project structure (if needed!):  
`django-admin startproject mysite .`

6. Apply migrations to database:  
`python manage.py migrate`

7. Create superUser for Django admin:  
`python manage.py createsuperuser`

---

### Run server:
`python manage.py runserver`

### Apply new changes:
**Create App, Make migrations, Apply migrations**

- _*optional:_ Creating app (Do not forget register it's name (bublik) in settings.py):  
`python manage.py startapp bublik`

- Create migrations, if has changes (bublik - app name, may be different):  
`python manage.py makemigrations bublik`

- APPLY MIGRATIONS (step 6 above)

---

### Deploy instruction on PythonAnywhere
1. Register an account on PythonAnywhere.com

2. Go to Account Tab and create API token if not exists

3. Make a Bash console and follow next instructions:

- `pip3.6 install --user pythonanywhere`

- `pa_autoconfigure_django.py https://github.com/YOUR_GITHUB/YOUR_REPO.git`
    - **(P.S. You can copy it from url) As example, this repo:**
    - `pa_autoconfigure_django.py https://github.com/leha404/django_bublik`

- `python manage.py createsuperuser`

---

P.S. Upload static files (CSS):  
1. Activate venv
2. python manage.py collectstatic
