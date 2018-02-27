from blog.settings.base_settings import *

DEBUG = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join((BASE_DIR), "staticfiles")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join((BASE_DIR), "staticfiles", 'media')
MEDIA_ROOT = os.path.join((BASE_DIR), "staticfiles", "media_root")

CRISPY_TEMPLATE_PACK = 'bootstrap3'
