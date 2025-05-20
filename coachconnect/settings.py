import os  # Required for optional STATICFILES_DIRS
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6@92!9c-)=n_^0s2$%&xfd1m9y@hfpp16d6588rlq#rmj#m0zs'
DEBUG = True
ALLOWED_HOSTS = []

# App definitions
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # ✅ needed for login/logout sessions
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coaching',  # ✅ your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coachconnect.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add global template dirs here later
        'APP_DIRS': True,  # ✅ Required to find templates inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coachconnect.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project4',
        'USER': 'postgres',
        'PASSWORD': '021007349',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = []



# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS, images)
STATIC_URL = 'static/'

# Optional: if you want a global static folder at project root (e.g. /static/)
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Auth redirects
LOGIN_REDIRECT_URL = 'session-index'
LOGOUT_REDIRECT_URL = 'home'

# Default PK field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
