# Navigation Project

This is project for tracking vehicles. 


## Installation
The project is written with Python 3.8.6 and Django ORM Framework.

```
git clone https://github.com/xephtar/NavigationProject.git
pip install -r requirements.txt
py manage.py migrate
```

## How to run App

```
py manage.py runserver
```

## Endpoints

There are three endpoints for use cases under the ```nagivation-api/``` path.

 - get-last-points
	 > It returns navigation records in last 48 hours per vehicle
 - bulk-create-vehicles
	 > It takes json array and creates vehicles
	 > The postman collections has example request body
 - bulk-create-navigation-records
	 > It takes json array and creates navigation records for vehicles
	 > The postman collections has example request body
