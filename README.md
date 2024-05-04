# django_bublik

## Pet project for photographers sales point

**Inspired by DjangoGirls:** 

https://tutorial.djangogirls.org/ru/django/

---

### Install Instructions:
1. Install virtual env: 
    - MacOS  
    `python3 -m venv myvenv`
    - Windows
    `python -m venv myvenv`


2. Run virtual environment:  
    - MacOS
    `source myvenv/bin/activate`
    - Windows
    `myvenv\Scripts\activate`


3. Update Python package manager (for Windows use python command, not python3):  
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

P.S. Upload static files (CSS):  
1. Activate venv
2. python manage.py collectstatic

---

### Windows problems

If you cannot activate vEnv and it's error:  
about_Execution_Policies

**Try this one:**  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Activate your env.  
To return policies back:  
`Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser`

---

### How to

**Want create one executable file for a project?**

- Make sure, that your PYTHONPATH has your project path
- Set policies remote signed for Windows (above)
- Activate vEnv
- Install pyinstaller (for a first time)
`pip install pyinstaller`
- Use next command 
`pyinstaller --onefile --add-data 'bublik/static;bublik/static' --add-data 'bublik/templates;bublik/templates' --hidden-import=django manage.py`
- Check dist folder
- Make sure to place your sqlite file with executable file together
- How activate? Use 'manage.exe runserver --noreload' command in a shell