# from flask import Flask
# from json import dumps
from src.load_data import load_data
from src.venues import closest_venues_by_category

# def defaultHandler(err):
#     response = err.get_response()
#     print('response', err, err.get_response())
#     response.data = dumps({
#         "code": err.code,
#         "name": "System Error",
#         "message": err.get_description(),
#     })
#     response.content_type = 'application/json'
#     return response

# APP = Flask(__name__)

# APP.config['TRAP_HTTP_EXCEPTIONS'] = True
# APP.register_error_handler(Exception, defaultHandler)


if __name__ == "__main__":
    load_data()
    print(closest_venues_by_category(49, -97, 3))

    # APP.run(port = 8080)
