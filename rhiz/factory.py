from flask import Flask
from flask.ext.security import Security

from flask_featureflags import FeatureFlag
from flask_mail import Mail

from rhiz.assets import assets
from rhiz.models import db, user_datastore
from rhiz.views.admin import admin
from rhiz.views.blog import register_routes as register_blog_routes


def create_app(config=None):
    app = Flask(__name__)

    # load configuration
    if config:
        app.config.from_object(config)
    else:
        app.config.from_object('rhiz.config.Default')
        app.config.from_envvar('RHIZ_APPLICATION_SETTINGS')

    security = Security()
    security.init_app(app, user_datastore)

    assets.init_app(app)
    db.init_app(app)
    admin.init_app(app)

    mail = Mail()
    mail.init_app(app)

    feature_flag = FeatureFlag()
    feature_flag.init_app(app)

    # register routes
    register_blog_routes(app)
    return app
