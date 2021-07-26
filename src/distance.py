"""Methods for finding the distance of venues

"""
from math import dist, sqrt

def distance_to_venue(venue, latitude, longitude):
    """Calculates and returns the distance to a venue using the Pythagorean theorem.
    
    Params:
        @venue: A venue object of the form:
            {
                name: "string",
                address: "string",
                categories: [
                    "string",
                    "string",
                    ...,
                    "string"
                ],
                latitude: number,
                longitude: number,
            }
        @latitude: Float used as the current latitude in the distance calculation.
        @longitude: Float used as the current longitude in the distance calculation.
    
    Returns:
        A float representing the straight line distance to the venue from the provided 
        coordinates.

    Raises:
        None
    """
    venue_lat = venue["latitude"]
    venue_long = venue["longitude"]

    distance = sqrt((latitude - venue_lat)**2 + (longitude - venue_long)**2)

    return distance