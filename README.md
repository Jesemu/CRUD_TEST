## CRUD_TEST
### by Jesús Serrano Muñoz
This project I'm going to implement a small Django application to manage (CRUD) users and their bank account data (IBAN). 
Required fields are first name, last name and IBAN. Data should be validated.

1. Administrators of the app should authenticate using a Google account
2. Administrators should be able to create, read, update and delete users
3. Restrict manipulation operations on a user to the administrator who created them
4. Use PostgreSQL as the database backend


## Installation:
To log in with Google I have used django-social-auth.
~~~
$ pip install social-auth-app-django
~~~~ 
After that we have to add the app __'social_django'__ to our installed apps.
And add the followins lanes:

~~~

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your Secret Key'
SOCIAL_AUTH_URL_NAMESPACE = 'social'


LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
~~~

To get your ID and Secret Key, you have to go to: Google Api https://console.developers.google.com/
On credenteials and create a new OAuth 2.0.

In redirects URLs you have to put: http://localhost:"your_port"/auth/complete/google-oauth2/

## Using Postgres
To use __Postgres__ we have to go to our settings.py file and change 
~~~
DATABASES = {
/****
/****
/****}
~~~

And put:

~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
~~~
The username and password are the defaults, if you want to use other, you only have to change there.

# To run the project you have:
1. Clone the repository
2. Go to root directory and execute:
~~~
sudo docker-compose build web
~~~
3. After that execute:
~~~
sudo docker-compose up -d
~~~
4. Do a migration:
~~~
sudo docker-compose exec web python manage.py makemgirations
sudo docker-compose exec web python manage.py migrate
~~~~ 
5. Open browser and check:  
http://localhost:2806  
http://127.0.0.0.1:2806
