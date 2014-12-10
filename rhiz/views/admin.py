from flask import current_app

from flask.ext.admin import Admin
from flask.ext.admin.contrib import sqla
from flask.ext.login import current_user

from rhiz.models import db, Post, User


class ModelView(sqla.ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()

    def inaccessible_callback(self, name, **kwargs):
        return current_app.login_manager.unauthorized()

admin = Admin(name='Rhizome Backend')

def is_accessible():
    return current_user.is_authenticated()

def inaccessible_callback(name):
    return current_app.login_manager.unauthorized()

admin.index_view.is_accessible = is_accessible
admin.index_view.inaccessible_callback = inaccessible_callback

admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(User, db.session))
