from decouple import config as env

from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings["sqlalchemy.url"] = env(
        "SQLALCHEMY_URL", settings["sqlalchemy.url"]
    )
    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
