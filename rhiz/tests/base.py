from flask.ext.testing import TestCase

# from rhiz.factory import create_app
from rhiz.models import db


class RhizomeTest(TestCase):

    def create_app(self):
        pass
        # return create_app(TestingConfig)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
