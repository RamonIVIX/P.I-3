"""
Django settings for telegrama project.
...
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%zwb__s&lpe2eepd%ojwh8+atndjzih7=$c_tf478%ph7=uihd'

DEBUG = True

ALLOWED_HOSTS = ['p-i-2-1.onrender.com', 'p-i-3-1.onrender.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # Adicionado para whiteNoise
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'telegrama',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Adicionado para whiteNoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'telegrama.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'telegrama.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'banco_de_dados_p_i3',
        'USER': 'banco_de_dados_p_i3_user',
        'PASSWORD': 'pyuODiUaGAidkgSKCUWnQIeL76FpG4BH',
        'HOST': 'dpg-d0nstsqdbo4c73a873s0-a.oregon-postgres.render.com',
        'PORT': '5432',
        # 'OPTIONS': {'sslmode': 'require'},  # descomente se precisar de SSL
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Pasta para collectstatic
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Onde ficam os estáticos locais

# WhiteNoise: compressão e cache para estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Login e Sessão
LOGIN_URL = '/login/'
SESSION_COOKIE_AGE = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
