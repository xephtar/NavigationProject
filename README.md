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

## Postman Collection

I added postman collection and environment to test API. There are example request bodies also.

### Whole collection is like below.

![collection](https://i.ibb.co/RpzHXHj/download-1.png)

### The get-last-points endpoint

![collection](https://i.ibb.co/LhLhYq2/download-2.png)

### The bulk-create-vehicles endpoint

![collection](https://i.ibb.co/47dmDvq/download-3.png)

### The bulk-create-navigation-records endpoint

![collection](https://i.ibb.co/djBS72C/download-4.png)

