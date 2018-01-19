import os
from blog.settings.base_settings import *

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
SECRET_KEY = os.environ.get('SECRET_KEY')
