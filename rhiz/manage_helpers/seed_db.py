from rhiz.models import db, user_datastore


def seed():
    user_datastore.create_user(
        email='scott.meisburger+test@rhizome.org',
        password='123')
    db.session.commit()

if __name__ == '__main__':
    print('Run as `python manage.py seed_db`')
