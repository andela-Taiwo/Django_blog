from blog.settings.base_settings import *

DEBUG = False

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
