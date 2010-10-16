# Django settings for hockey_register project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
_PROJECT_ROOT = '/home/pontiffx/media/code/savages-hockey/hockey_register'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           
DATABASE_NAME = '%s/../data/DB.data' % _PROJECT_ROOT 
DATABASE_USER = ''             
DATABASE_PASSWORD = ''        
DATABASE_HOST = ''           
DATABASE_PORT = ''          

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True


MEDIA_ROOT = '%s/media/' % _PROJECT_ROOT

MEDIA_URL = '/m/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'k23rKJRN3FNFnKF0FFKF.FW;PEFF'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#	'django.contrib.csrf.middleware.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'hockey_register.urls'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'

TEMPLATE_DIRS = (
	'%s/templates' % _PROJECT_ROOT, 
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
	'django.contrib.admin',
	'hockey_register.register',
)
