import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    },
}

INSTALLED_APPS = (
    'db',
    'django_extensions',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = 'wev!u_r4q1or2ztn$)ed5asm_+&($@ab(+bhc%8reak9niy9vv'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True