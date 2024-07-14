#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Set environment variables
export FLASK_APP=src.app
export FLASK_ENV=development
export PYTHONPATH=/Users/nimit-rastogi/Desktop/Bitespeed 

# Run the Flask application
flask run
