## Cheatsheet (Django)

###### Checking the Python version
`python --version`

###### Starting a Django Project
 - `pip install django`
 - `django-admin startproject notes`

###### Running a the Django server
- `python manage.py runserver`

###### Running Migrations
- `python manage.py migrate`









###### Common Commands
- Change Directory - `cd <folder-name>`


#### Possible error(s)

##### TLS version error

######Problem
Could not fetch URL https://pypi.python.org/simple/django/: There was a problem confirming the ssl certificate: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:600) - skipping
######Solution
Run this command:

`curl https://bootstrap.pypa.io/get-pip.py | python`
