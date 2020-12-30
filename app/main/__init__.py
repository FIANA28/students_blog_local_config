from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

# a context processor can also make functions available to templates 
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

