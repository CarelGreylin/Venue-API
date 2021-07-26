from src.error import InputError
from flask import Flask, request
from json import dumps
from src.load_data import load_data
from src.venues import closest_venues_by_category

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": err.name,
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

@APP.route("/venues/by_category", methods = ["GET"])
def get_channels_by_category():
    """API route that performs error handling before calling the 
    closest_venues_by_category function to return the result in JSON format.
    
    Raises InputError for any invalid URL parameters provided.
    """
    # Get arguments from request
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    limit = request.args.get("limit")

    # Check presence and validate coordinates
    if latitude and longitude:
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except:
            raise InputError("Longitude and latitude should be floats.")
    else:
        raise InputError("Missing coordinate parameter")
    
    # Check and validate limit parameter
    if limit:
        try:
            categories = \
                closest_venues_by_category(latitude, longitude, int(limit))
        except:
            raise InputError("Limit should be an integer.")
    else:
        categories = closest_venues_by_category(latitude, longitude)
    
    # Return result in JSON format
    return dumps(categories)

if __name__ == "__main__":
    load_data()

    APP.run(port = 8080)
