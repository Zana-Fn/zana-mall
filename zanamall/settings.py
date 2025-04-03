import os
from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_FILE_STORAGE="storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID="bbaa294f-1c77-44c1-a4c4-16e070ff98c2"
AWS_SECRET_ACCESS_KEY="e39a23a6371c510286878577094cb00469fa3b04bf02a6ebaef9fbb15140c472"
AWS_STORAGE_BUCKET_NAME="myimgcloud"
AWS_S3_ENDPOINT_URL="https://s3.ir-thr-at1.arvanstorage.com"
AWS_S3_ADDRESSING_STYLE="virtual"
AWS_S3_CUSTOM_DOMAIN=f"{AWS_STORAGE_BUCKET_NAME}.s3.ir-thr-at1.arvanstorage.com"
MEDIA_URL=f"https://{AWS_S3_CUSTOM_DOMAIN}/"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@y-6h#9(r6iwt-ka@m%civ^#6)0m-k#rd2%t$fqiru+zw8ndfo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://zana-mall.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mall',
    'cart',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'zanamall.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'zanamall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': 
    dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#postgresql://mydatabase_046p_user:Nrjg3KBUdeu0ujvKaaHIpnDRVgn7mQNp@dpg-cvmmfih5pdvs73898hrg-a/mydatabase_046p