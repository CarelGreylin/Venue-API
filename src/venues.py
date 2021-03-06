"""Methods for retrieving venues from the database.

Searches the venues database and retrieves venues based on certain parameters.
"""

import src.data as d
from math import dist

def closest_venues_by_category(latitude, longitude, limit=d.DEFAULT_LIMIT):
    """Returns venues sorted by their distance (increasing) from 
    @latitude and @longitude. Venues are structured under their categories. 
    Categories with the most venues appear first, and are then sorted 
    alphabetically. There are at most @limit venues for each category.

    Params:
        @latitude: Float used as the current latitude in the distance calculation.
        @longitude: Float used as the current longitude in the distance calculation.
        @limit: The maximum amount of venues to return under each category.

    Returns:
        A list of objects in the form:
            {
                "category": "Category1",
                "venues": [
                    {
                        "name": "Venue1",
                        "address": "Address1"
                    },
                    {
                        "name": "Venue2",
                        "address": "Address2"
                    },
                ]
            }
    
    Raises:
        None
    """
    # Calculate distance of all venues and collect categories in a dictionary.
    venues_distance = []
    categories = {}
    for venue in d.VENUES:
        venue_details = venue
        venue_details["distance"] = dist(
            [venue["latitude"], venue["longitude"]], 
            [latitude, longitude]
        )
        venues_distance.append(venue_details)

        # Add category to the dictionary as a key with an empty list
        for category in venue["categories"]:
            categories[category] = []

    # Sort venues by distance
    sorted_venues = sorted(venues_distance, key= lambda k: k["distance"])

    # Insert venues into their category lists until limit is reached.
    for venue in sorted_venues[:limit]:
        for category in venue["categories"]:
            categories[category].append({
                "name" : venue["name"],
                "address" : venue["address"],
            })

    # Construct the shape of the final return value
    categories = [
        {
            "category" : category,
            "venues" : categories[category],
        }
        for category in categories if len(categories[category]) > 0
    ]

    # Sort categories by the amount of venues found and then alphabetically
    sorted_categories = sorted(
        categories, 
        key= lambda k: (limit - len(k["venues"]), k["category"].lower())
    )

    return sorted_categories
