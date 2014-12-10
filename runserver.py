import logging

from rhiz.factory import create_app


app = create_app()
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app.debug = True
    logging.basicConfig(level=logging.DEBUG)
    app.run()
