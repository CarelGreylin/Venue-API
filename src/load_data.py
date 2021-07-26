"""
    Functions for reading venue data into VENUES variable from csv file.
"""
from src.data import VENUES, DATA_FILE
import csv

def load_data(file_path):
    file = open(file_path, newline='')
    csv_reader = csv.DictReader(file)
    for venue in csv_reader:
        # Split categories
        venue["categories"] = venue["categories"].split(',')
        VENUES.append(venue)
    file.close()

if __name__ == "__main__":
    load_data(DATA_FILE)
    print(VENUES)