from flask import render_template
from flask_featureflags import is_active_feature

from rhiz.models import Post


def register_routes(app):
    @app.route('/')
    def homepage():
        return render_template('hello.html')

    @app.route('/blog/')
    @is_active_feature('blog')
    def blog():
        posts = Post.query.all()
        return render_template('blog/list.html', posts=posts)
