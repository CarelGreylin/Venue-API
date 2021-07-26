"""Methods for retrieving venues from the database.

Searches the venues database and retrieves venues based on certain parameters.
"""

import src.data as d
import bisect
from src.distance import distance_to_venue as distance

def closest_venues_by_category(latitude, longitude, limit=d.DEFAULT_LIMIT):
    """Returns at most @limit venues sorted by their distance (increasing) from 
    @latitude and @longitude. Venues are structured under their categories and
    seconderily sorted alphabetically.

    Params:
        @latitude: Float used as the current latitude in the distance calculation.
        @longitude: Float used as the current longitude in the distance calculation.
        @limit: The maximum amount of venues to return under each category.

    Returns:
        A list of objects in the form:
            {
                "category": Category1,
                "venues": [
                    {
                        "name": Venue1,
                        "address": Address1
                    },
                    {
                        "name": Venue2,
                        "address": Address2
                    },
                ]
            }
    
    Raises:

    """
    # Calculate distance of all venues and get categories
    venues_distance = []
    categories = {}
    for venue in d.VENUES:
        venue_details = venue
        venue_details["distance"] = distance(venue, latitude, longitude)
        venues_distance.append(venue_details)
        for category in venue["categories"]:
            categories[category] = []

    # Sort venues by distance
    sorted_venues = sorted(venues_distance, key= lambda k: k["distance"])

    # Insert venues into list until limit is reached.
    for venue in sorted_venues:
        for category in venue["categories"]:
            if len(categories[category]) < limit:
                categories[category].append({
                    "name" : venue["name"],
                    "address" : venue["address"],
                })

    categories = [
        {
            "category" : category,
            "venues" : categories[category],
        }
        for category in categories
    ]

    # Sort categories by the amount of venues found and then alphabetically
    sorted_categories = sorted(
        categories, 
        key= lambda k: (limit - len(k["venues"]), k["category"])
    )

    return sorted_categories
