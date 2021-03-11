#!/bin/bash

export FLASK_ENV=development

# run our server locally:
cd source; FLASK_APP=source/endpoints flask run --host=127.0.0.1 --port=8000
