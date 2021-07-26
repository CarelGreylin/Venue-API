"""Functions for reading data into the database.

Reads and formats csv data into the VENUES variable using the csv module.
"""
from src.data import VENUES, DATA_FILE
import csv

def load_data(file_path):
    """Fill database with data from @file_path
    
    Read data line by line from a csv file and format it into a dictionary.

    Args:
        @file_path: String with the relative or absolute path to the csv file
            to read in from. 

    Returns:
        None

    Raises:
        None
    """
    file = open(file_path, newline='')

    # Formats each line into a dictionary, keys taken from first line
    csv_reader = csv.DictReader(file)

    for venue in csv_reader:
        # Split categories
        venue["categories"] = venue["categories"].split(',')
        VENUES.append(venue)
    file.close()

if __name__ == "__main__":
    load_data(DATA_FILE)
    print(VENUES)