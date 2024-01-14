#!/usr/bin/python3
""" Starts a Flash Web Application """
<<<<<<< HEAD
=======
import uuid
>>>>>>> f7ca81b5d757da9e2697dcb041c742cd287be516
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
<<<<<<< HEAD
import uuid
=======
>>>>>>> f7ca81b5d757da9e2697dcb041c742cd287be516
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


<<<<<<< HEAD
@app.route('/2-hbnb/', strict_slashes=False)
=======
@app.route('/2-hbnb', strict_slashes=False)
>>>>>>> f7ca81b5d757da9e2697dcb041c742cd287be516
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)
<<<<<<< HEAD

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())
=======
    cache_id = str(uuid.uuid4())

    return render_template('1-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)
>>>>>>> f7ca81b5d757da9e2697dcb041c742cd287be516


if __name__ == "__main__":
    """ Main Function """
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5001)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> f7ca81b5d757da9e2697dcb041c742cd287be516
