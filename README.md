# flask-xd

PyPi Link:
https://pypi.org/project/flask-xd/

This package sets up a working directory for a flask app. You can choose either an empty template or one setup
with auth/user services already working.

# Installation
1. pip install 'flask-xd' then run 'flasksetup'
2. Follow prompts
3. Once the directory has been created go into it and set up a virtual environment
4. pip install -r requirements.txt
5. set envriontment variables for 
  - DATABASE_URL - postgres database url
  - SECRET_KEY - jwt secret key
  - BOILERPLATE_ENV - Dev, test, or prod

6. pip uninstall flask-xd
7. python manage.py run

 # Mac/Linux
 Setting up and entering venv:
  python3 -m venv venv
  source venv/bin/activate
 
 Environ var ex:
  export DATABASE_url='your-url'
 
 # Windows
 Setting up and entering venv:
  python3 -m venv venv
  .\venv\Scripts\activate
 
 environ var ex:
   $env:DATABASE_URL='your-url'
