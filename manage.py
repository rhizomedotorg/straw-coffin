import sys
import sqlalchemy

from flask.ext.assets import ManageAssets
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager


from rhiz import models
from rhiz.factory import create_app
from rhiz.models import db


app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('assets', ManageAssets)

@manager.shell
def _make_context():
    return dict(app=app, db=db, models=models)

@manager.command
@manager.option('-v', '--verbose', dest='verbose', default=False)
def seed_db(verbose=False):
    from rhiz.manage_helpers.seed_db import seed
    if not verbose:
        db.engine.echo = False

    sys.stdout.write(u'Seeding the database.\n')
    seed()
    return 0

@manager.command
@manager.option('-v', '--verbose', dest='verbose', default=False)
def soft_reset(verbose=False):
    if not verbose:
        db.engine.echo = False

    db.drop_all()
    db.create_all()
    seed_db()
    return 0

@manager.command
@manager.option('-v', '--verbose', dest='verbose', default=False)
def hard_reset(verbose=False):
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    meta = sqlalchemy.MetaData(engine)
    meta.reflect()
    meta.drop_all()
    MigrateCommand._commands['upgrade'].run()
    seed_db()

if __name__ == '__main__':
    manager.run()
