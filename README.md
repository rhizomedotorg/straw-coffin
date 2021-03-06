straw-coffin
============

Rhizome site in Flask

```$ ln -s ../../../pre-commit.sh /path/to/straw-coffin/.git/hooks/pre-commit```

```
$ cp /path/to/straw-coffin/sample_config.py ~/local_config.py
$ export RHIZ_APPLICATION_SETTINGS=~/local_config.py
```

Add the above `export` to your shell's init script (`.bash_profile` for some) so that `RHIZ_APPLICATION_SETTINGS` gets set permanently.

You will add/edit settings in `~/local_config.py` to override [default config](rhiz/config.py).

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py db upgrade
$ python manage.py seed_db
$ python manage.py runserver
```

Useful docs
----

- [Flask-Security](https://pythonhosted.org/Flask-Security/)
- [Flask-Assets](http://flask-assets.readthedocs.org/en/latest/)
- [Flask-FeatureFlags](https://github.com/trustrachel/Flask-FeatureFlags)
- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
