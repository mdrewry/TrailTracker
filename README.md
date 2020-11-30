# TrailTracker

#### Contributors
* Mark Drewry
* Rohan Samanta
* Nickolas Phen
* Andrew Gil

#### Technology
* Python, Django, SQLite, HTML, CSS

#### Description
* Record experiences of a hike.
* Add and view statistics for different hike entries.
* Add photos of the hikes and view trail locations on an interactive map. 

#### Link
* https://github.com/mdrewry/TrailTracker

#### Pip Packages
* asgiref v3.2.10
* Django v3.1.2
* django-crispy-forms v1.9.2
* django-google-maps v0.12.2
* django-map-widgets v0.3.0
* Pillow v8.0.0
* pytz v2020.1
* sqlparse v0.4.1

# Installation Guide

#### Install SQLite
* sudo apt update
* sudo apt-get install sqlite3

#### Install Pip Packages
* pip install -r requirements.txt

#### (Option 1) Run App With Script
* bash start

#### (Option 2) Run App Without Script
* python manage.py makemigrations
* python manage.py sqlmigrate dashboard 0001
* python manage.py migrate
* python manage.py runserver
