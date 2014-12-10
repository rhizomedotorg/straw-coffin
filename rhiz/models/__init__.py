from flask.ext.security import SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from post import Post
from user import User, Role

__all__ = ['Post', 'User', 'Role']

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
