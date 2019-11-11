from flask import Blueprint

package = Blueprint('package', __name__)

from . import views, error
