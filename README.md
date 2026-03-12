# The Ultimate Django Series: Part 2

required: Python 3.12 version

## Setting Up the Project

```sql
CREATE DATABASE storefront2
```

```bash
pip install -r requirements.txt
python manage.py migrate
```

Export seed.sql

```bash
python manage.py createsuperuser
```

# Building RESTful APIs with Django REST Framework

## What are RESTfull APIs?

RESTFULL?  
<b>Re</b>presentational <b>S</b>tate <b>T</b>ransfer

### Benefits

 - Fast
 - Scalable
 - Reliable
 - Easy to understand
 - Easy to change

Resources - Representations - Http Methods

## Resources

 - Product
 - Collection
 - Cart

URL - Uniform Resource Locator

http://rovshenbuy.com/products/
http://rovshenbuy.com/products/1/
http://rovshenbuy.com/products/1/reviews/
http://rovshenbuy.com/products/1/reviews/1/

## Resource Representations

 - HTML
 - XML
 - JSON

```py
class Product(models.Model):
    title = models.CharField()
    price = models.DecimalField()
```

JSON - JavaScript Object Notation

```json
{
    "name": "Rovshen",
    "age": 25,
    "is_online": true,
    "employer": {},
    "interests": []
}
```

## HTTP Methods

 - GET
 - POST
 - PUT
 - PATCH
 - DELETE

***

Creating a Product  
POST /products/  
```json
{
    "title": "...",
    "price": 10
}
```

***

Updating a Product  
PUT     /products/1/  
PATCH   /products/1/  
```json
{
    "title": "...",
    "price": 10
}
```

***
Deleting a Product  
DELETE /products/1/  
```json
```

## Installing Django REST Framework

```bash
pip install djangorestframework
pip freeze > requirements.txt
```

## Creating API Views

<pre>
Django         - HttpRequest -> HttpResponse  
REST Framework - Response    -> Response
</pre>

## Creating Serializers

REST Framework - JSONRenderer - render(dict)

Serializer - Converts a model instance to a dictionary

## Creating Custom Serializer Fields

API Model != Data Model

Data Model -> Implementation (models.Model)  
API Model -> Interface (serializers.Serializer)  

## Serializing Relationships

 - Primary key
 - String
 - Nested Object
 - Hyperlink

# Designing and Implementing a Shopping Cart API

## Designing the API

### Operations

 - Create a cart
 - Add items to a cart
 - Update the quantity of items
 - Remove items from a cart
 - Get a cart with its items

| Operation        | METHOD | url                  | request       | response |
|------------------|--------|----------------------|---------------|----------|
| Creating a Cart  | POST   | /carts/              | {}            | cart     |
| Getting a Cart   | GET    | /carts/:id           | {}            | cart     |
| Deleting a Cart  | DELETE | /carts/:id           | {}            | {}       |
| Adding an Item   | POST   | /carts/:id/items/    | {prodId, qty} | item     |
| Updating an Item | PATCH  | /carts/:id/items/:id | {qty}         | {qty}    |
| Deleting an Item | DELETE | /carts/:id/items/:id | {}            | {}       |

## Revisiting the Data Model

GUID: Globally Unique Identifier

Premature optimization is the root of all evils. ( - Donald Knuth)

# Django Authentication System

## Django Authentication System

tables begin with auth - auth_user
