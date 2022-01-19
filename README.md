# ZipAirlines API

An API built with Django RestFramework.

## Getting up and running

The steps below will get you up and running with a local development environment. We assume you have the following installed:

- pip
- virtualenv

First make sure to create and activate a virtualenv, then open a terminal at the project root and install the requirements for local development:

```bash
  $ pip install -r requirements.txt

```
Run django migrations command for creating table:

```bash
  $ python manage.py makemigrations
  $ python manage.py migrate

```
You can now run the usual Django runserver command (replace yourapp with the name of the directory containing the Django project):

```bash
  python yourapp/manage.py runserver

```
#### Usage

Open the browser to http://127.0.0.1:8000

Input the data of plane id and Passenger capacity in Json data format in the content box and click the Post button.

```bash
  {
    "id": 1,
    "passenger": 110
  }
```
It is allowed for input of 10 airplanes, so Post the data 10 times with their ids and passenger capacities.

API prints the total airplane fuel consumption per minute and maximum minutes able to fly. It can be accessed at:



```bash
  http://127.0.0.1:8000/results

```

## Testing

For testing, you can use these commands:

```bash
  $ python manage.py test api.tests

```

For coverage report, you can use these commands:

```bash
  $ coverage run manage.py test api.tests
  $ coverage report -m

```
