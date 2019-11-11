from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_pagedown import PageDown
import os



bootstrap = Bootstrap()
moment = Moment()
pagedown = PageDown()


def create_app():
    SECRET_KEY = os.urandom(32)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    bootstrap.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)

    from website.pages.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from website.pages.package import package as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/package')

    return app
