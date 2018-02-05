from blog.settings.base_settings import *
import dj_database_url
from decouple import config


DEBUG = False
ADMINS = (('@memunat', 'taiwo.sokunbi@andela.com'), )
db_from_env = dj_database_url.config()
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500
