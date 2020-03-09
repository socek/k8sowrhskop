from pyramid.view import view_config

from .. import models


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home(request):
    return {'one': 'one', 'project': 'faker'}


@view_config(route_name='dbcheck', renderer='../templates/dbcheck.jinja2')
def dbcheck(request):
    query = request.dbsession.query(models.MyModel)
    one = query.filter(models.MyModel.name == 'one').first()
    return {'one': one}
