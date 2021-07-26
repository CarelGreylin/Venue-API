""" File for storing constants and database files.

Venues database stored as a list of venues where each venue is of the form:
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
"""
VENUES = []

# Constants
DEFAULT_LIMIT = 10

# Files
DATA_FILE = "venues.csv"