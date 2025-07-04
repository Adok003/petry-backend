#!/bin/sh
gunicorn main.wsgi:application --bind 0.0.0.0:8000
