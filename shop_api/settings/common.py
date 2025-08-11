"""
Django settings for shop_api project.
"""

from pathlib import Path
import datetime, os
from dotenv import load_dotenv
load_dotenv()
import pytz


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_FOLDER = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',

    # DRF
    'rest_framework',
    'rest_framework_jwt',

    # Project apps
    'apps.users',
    'apps.shop',
    # 'shop_api',
    'shop_api.apps.ShopApiConfig',

    # Frontend
    'corsheaders'

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'users.User'
SHELL_PLUS = 'ipython'

SHELL_PLUS_PRE_IMPORTS = [
    ('datetime', ('datetime', 'timedelta')),
]

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_DEFAULT_QUEUE = os.getenv('CELERY_DEFAULT_QUEUE')
CELERY_DEFAULT_EXCHANGE = os.getenv('CELERY_DEFAULT_QUEUE')
CELERY_DEFAULT_ROUTING_KEY = os.getenv('CELERY_DEFAULT_QUEUE')
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND=os.getenv('CELERY_RESULT_BACKEND')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

REDIS_URL = os.getenv('REDIS_URL')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# MailCatcher
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL  = os.getenv('DEFAULT_FROM_EMAIL')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.users.services.auth.authentication_service.JSONWebTokenAuthentication',
    ),
    'EXCEPTION_HANDLER': 'core.utils.exception_handler.exception_handler_wrapper',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25
}

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

JWT_AUTH = {
    'JWT_SECRET_KEY': JWT_SECRET_KEY,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),
}

TIMEOUT_IN_MINUTES_TIME = int(os.environ.get('TIMEOUT_IN_MINUTES_TIME', 0))

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_DATE_FORMATS = ('%m/%d/%Y', '%Y-%m-%d')

SERVER_TIMEZONE = pytz.UTC

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ADMIN_MAX_LOGIN_ATTEMPTS = 3
ADMIN_NEW_LOGIN_TIMEOUT_MINUTES = 15


# the name of the versions will be added to the endpount name as
# prefix: {HOST}/{version}/{endpoint_name}
# In addition endpoint should be placed
# into urlpatterns to urls_{version}.py file
API_VERSIONS = ('v1', 'v2', )

# Logging configuration
# based on Loguru (https://github.com/Delgan/loguru)
LOGURU_BACKTRACE = True
LOGURU_DIAGNOSE = True
LOG_LEVEL = "INFO"
LOGURU_FORMAT = (
    "[<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>]"
    "[<level>{level}</level>] "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
)

CORS_ALLOW_ALL_ORIGINS = True

