#!/usr/bin/python3
""" Flask Application """
from flask import Flask, abort, render_template, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import environ
from flask_cors import CORS
from flasgger import Swagger
import os
from werkzeug.exceptions import HTTPException

# Global Flask Application Variable: app
app = Flask(__name__)


swagger = Swagger(app)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 errors, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

@app.errorhandler(400)
def handle_400(exception):
    """
    handles 400 errros, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(Exception)
def global_error_handler(err):
    """
        Global Route to handle All Error Status Codes
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not found"
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': err}
        code = 500
    return make_response(jsonify(message), code)


def setup_global_errors():
    """
    This updates HTTPException Class with custom error function
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # initializes global error handling
    setup_global_errors()
    # start Flask app
    """ Main Function """
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', 5001)
    app.run(host=host, port=port, threaded=True, debug=True)
