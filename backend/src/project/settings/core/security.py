
from configurations import Configuration

class Security(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'ezn21+vvw9p$49fx#f^46vbs&cv!1$z%(tn2ln%4)(w-c@&c2k'

    # Password validation
    # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
