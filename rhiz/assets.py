from flask.ext.assets import Environment, Bundle


assets = Environment()

js = Bundle('jquery-1.11.1.js', 'base.js',
            # Bundle(
            #     'all.coffee',
            #     filters=['coffeescript']
            # ),
            filters='jsmin', output='gen/packed.%(version)s.js')

css = Bundle('all.scss',
             filters='scss', output='gen/css_all.%(version)s.css')

assets.register('js_all', js)
assets.register('css_all', css)


# def register_assets_config(app):
#     with app.app_context():
#         # only auto-build assets in dev env
#         if app.config['ENVIRONMENT'] in ('sandbox', 'test'):
#             assets.auto_build = True
#         else:
#             assets.auto_build = False
