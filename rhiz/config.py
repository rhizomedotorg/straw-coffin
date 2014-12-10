class Default(object):
    DEBUG = False
    TESTING = False
    ASSETS_AUTOBUILD = False

    FEATURE_FLAGS = {
        'blog' : True,
    }

    # Flask-Security
    SECURITY_PASSWORD_HASH = 'sha256_crypt'
    SECURITY_PASSWORD_SCHEMES = ['sha256_crypt', 'django_pbkdf2_sha256']

    SECURITY_EMAIL_SENDER = 'no-reply@rhizome.org'
    # SECURITY_UNAUTHORIZED_VIEW = 'login'

    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True

    # SECURITY_DEFAULT_REMEMBER_ME = True

class Testing(Default):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
