from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mq3@3%aaqdd^#s&ykeb+&peuyb15!kr=lh)!2^%m5@3h5n=xwa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'mozilla_django_oidc',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    # ...
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_oidc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'django_oidc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# mozilla-django-oidc

# http://localhost:8080/realms/myrealm/
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_IDP_SIGN_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAh0IIhZADtWY69wH0BIQ94Mgz7MfcrDeNTI8oqyPtfq0liJ5CzXQ3X/3bGXyyii6fJkLwUS/WbSSoglH8msw1msD+iVkJ+WXB+fDUb/3jjmcA6rdmoQDxK+zLJad50eps2E2aBfEXlLHRebky5w83JJdamX3O/UJLD/xAC9vzO+56XWfSI6dgP7bBXTkcMSAkb0Ng7KmF8cFHNhp6+iO5IU7zKWjwMUob6Q6EixjSVjZmpqniOf9S74l72vi1tT//FkyMfbragtpVbId76K9Bd+gMnh/F3ska2jg3h74HiHnIXFpIqz1cSnUpaQCiwv6AgodLzGWf9DqtsiyuIMhlTwIDAQAB
-----END PUBLIC KEY-----"""

OIDC_RP_CLIENT_ID = "conf-client"
OIDC_RP_CLIENT_SECRET = "I4rSpkw7Dp7sHVgMWYzwboStV9DotTTp"

# http://localhost:8080/realms/myrealm/.well-known/openid-configuration
OIDC_OP_JWKS_ENDPOINT = "http://localhost:8080/realms/myrealm/protocol/openid-connect/certs"
OIDC_OP_AUTHORIZATION_ENDPOINT = "http://localhost:8080/realms/myrealm/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = "http://localhost:8080/realms/myrealm/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = "http://localhost:8080/realms/myrealm/protocol/openid-connect/userinfo"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
