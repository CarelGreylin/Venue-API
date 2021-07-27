#!/bin/bash
python3 -m server &
pytest
pytest --durations=0