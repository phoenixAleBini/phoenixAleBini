
import os        #agregado para personalizar el panel admin
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# PARA PRODUCCIÓN cambiar clave encriptada!
SECRET_KEY = 'django-insecure-y1&yhp!5z5xrq)bz#+^4q)rlya3wyb)9rw727f30)i@(ts9+_j'

# PARA PRODUCCIÓN  va en false!
DEBUG = True

# PARA PRODUCCIÓN  desde  donde recibe peticiones.... si fuera desde cualquiera:  0.0.0.0.
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
#    'admin_interface',  #agregado para personalizar el panel admin
 #   'colorfield',       #agregado para personalizar el panel admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appOASIS',
]


X_FRAME_OPTIONS = "SAMEORIGIN"                #agregado para personalizar el panel admin
#SILENCED_SYSTEM_CHEC'ALLOWALL'KS = ["security.W019"]    #agregado para personalizar el panel admin



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# donde están todas las urls....
ROOT_URLCONF = 'proyectOASIS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'proyectOASIS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "OASIS",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "Madrid.2021",
        "HOST": "localhost",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "es-eu"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True









# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'appOASIS/static')
    
]

# PARA PRODUCCIÓN  http://..........
STATIC_URL = '/static/' 



#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')   #agregado para personalizar el panel admin

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'