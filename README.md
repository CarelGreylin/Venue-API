# Streamplate Server Technical Task

## How to use
### On Windows
Run `py -3 -m server` to start the Flask server and send request via web browser or REST client **OR** run simply run the provided batch file to start up the server and run 6 premade tests using pytest: `./test.bat`. These tests will display their slowest runtimes after execution.

### On Linux
Run `python3 -m server` to start the Flask server and send request via web browser or REST client **OR** run simply run the provided script file to start up the server and run 6 premade tests using pytest: `sh test.sh`. These tests will display their slowest runtimes after execution.

**NOTE:** Linux script is untested.

### Required packages
- Flask (and dependencies)
- pytest

## About
Python API that returns a list of categories and the
venues under those categories that are closest to the coordinates provided. Follows the
requirements:
- Accepts arguments:
    - latitude (required)
    - longitude (required)
    - limit (optional): Limits the closest X venues that will be used to generate the categories and sort them under. If no limit is provided, the closest 10 venues will be used and sorted.
- Returns a list of objects in the format:
```json
[
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
    },
        {
        "category": Category2,
        "venues": [
            {
                "name": Venue3,
                "address": Address3
            },
        ]
    },
]
```

- The list of categories is sorted in descending order of how many venues each category has, then in alphabetical order.
- The list of venues for each category is sorted in ascending order of venue's distance from the provided coordinates.