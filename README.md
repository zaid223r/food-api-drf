
Food Info API 
===
A comprehensive web API for accessing food-related information, built using Django Rest Framework (DRF).
## Table of Contents

[TOC]

## Introduction
The Food Info Web API provides access to food-related data, including nutritional information and recipes. Powered by Django Rest Framework, this API offers a RESTful interface for easy integration into web and mobile applications.

## Beginners Guide

If you are a total beginner to this, start here!

1. Clone the repository:
    ```bash
    git clone https://github.com/zaid223r/food-api-drf.git
    ```
2. Navigate to the project directory:
    ```bash
    cd food-api-drf
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```
The application should now be accessible at http://localhost:8000.

Usage
---
To start using the API, you can explore the available endpoints using tools like Postman or curl. Refer to the API Endpoints section below for details on the available endpoints.



Features
---
* Simple and Intuitive: Easy-to-use API with five endpoints for accessing food-related information.
* RESTful Interface: Follows REST principles for intuitive and standardized API interactions.


API Endpoints
---
* GET /food/ : Retrieve a list of all available food items.
* GET /food/{food_id}/ : Retrieve details of a specific food item by ID.
* POST /food/ : Create a new food item.
* PUT /food/{food_id}/ : Update food details.
* DELETE /food/{food_id}/ : Delete specific record.

Example
---

**GET /food/1**
```json
{
  "Food": {
    "id": 1,
    "name": "Blue Crap",
    "type": "seafood",
    "calories": 100,
    "protein": 20,
    "sugar": 0
  }
}
```