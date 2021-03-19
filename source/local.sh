#!/bin/bash

export FLASK_ENV=development

# run our server locally:
FLASK_APP=endpoints flask run --host=127.0.0.1 --port=8000
