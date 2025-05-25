"""
Django settings for telegrama project.
...
"""

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = [BASE_DIR / "static"]

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # importante para o Render
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # opcional, se você usa /static/


STATIC_URL = 'static/'


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%zwb__s&lpe2eepd%ojwh8+atndjzih7=$c_tf478%ph7=uihd'

    # SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['p-i-2-1.onrender.com', 'localhost', '127.0.0.1']



    # Application definition

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',  
        'telegrama',
    ]

LOGIN_URL = '/login/' 

    # Sessão dura x segundos
SESSION_COOKIE_AGE = 3600

    # Expira só depois desse tempo, portanto = false
SESSION_EXPIRE_AT_BROWSER_CLOSE = False



MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
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



#DATABASES = {
#        'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#            'NAME': 'Alunos',
#            'USER': 'postgres',
#            'PASSWORD': '1234',
#            'HOST': 'localhost',
#            'PORT': '5432',
#            }
#    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'banco_de_dados_p_i3',
        'USER': 'banco_de_dados_p_i3_user',
        'PASSWORD': 'pyuODiUaGAidkgSKCUWnQIeL76FpG4BH',
        'HOST': 'dpg-d0nstsqdbo4c73a873s0-a.oregon-postgres.render.com',
        'PORT': '5432',
        #'OPTIONS': {
#           # 'sslmode': 'require',  # importante para conexão segura no Render
        }
    }




    #DATABASES = {
    #    'default': {
    #        'ENGINE': 'django.db.backends.sqlite3',
    #        'NAME': BASE_DIR / 'db.sqlite3',
    #    }
    #}


    # Password validation
    # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'