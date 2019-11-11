from flask import render_template
from . import package


@package.route('/', methods=['GET', 'POST'])
def index():

    return render_template('/package/index.html')