from pathlib import Path
import environ
import os

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default='').split(",")

PUBLIC_IP = env("PUBLIC_IP")
FASTAPI_PORT = env("FASTAPI_PORT")

OAUTH_CLIENT_ID = env("OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = env ("OAUTH_CLIENT_SECRET")
KOREAUNIV_OPENAPI_CLIENT_ID=env("KOREAUNIV_OPENAPI_CLIENT_ID")
KOREAUNIV_OPENAPI_CLIENT_SECRET=env("KOREAUNIV_OPENAPI_CLIENT_SECRET")

STUDENT_SYNC_URL= env("STUDENT_SYNC_URL")
REPO_SYNC_URL=env("REPO_SYNC_URL")
REPO_COMMIT_SYNC_URL=env("REPO_COMMIT_SYNC_URL")
REPO_ISSUE_SYNC_URL=env("REPO_ISSUE_SYNC_URL")
REPO_PR_SYNC_URL=env("REPO_PR_SYNC_URL")
REPO_CONTRIBUTOR_SYNC_URL=env("REPO_CONTRIBUTOR_SYNC_URL")
COURSE_OS_SYNC_URL=env("COURSE_OS_SYNC_URL")
COURSE_CAPSTONE_SYNC_URL_1=env("COURSE_CAPSTONE_SYNC_URL_1")
COURSE_CLOUD_SYNC_URL=env("COURSE_CLOUD_SYNC_URL")
COURSE_SW_PROJECT_SYNC_URL=env("COURSE_SW_PROJECT_SYNC_URL")
COURSE_CAPSTONE_SYNC_URL_2=env("COURSE_CAPSTONE_SYNC_URL_2")



# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework'
]

THIRD_PARTY_APPS = [
    'corsheaders'
]

LOCAL_APPS = [
    "core",
    "account",
    "repo",
    "course",
    "login",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'HOST': env('DB_HOST'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = 'account.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_URLS_REGEX = r"^/api/.*$"
#여기서 
CORS_ORIGIN_ALLOW_ALL = True
#여기까지 


if DEBUG:
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer'
        ]
    }
else:
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer'
        ]
    }
