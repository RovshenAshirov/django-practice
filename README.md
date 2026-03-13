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

## Customizing the User Model

### Extend User

`User <- AppUser`  
For storing attributes related to authentication

### Create Profile

`Profile -> User`  
For storing non-auth related attributes

<pre>
sales     -  Customer
hr        -  Employee
training  -  Student
</pre>

## Extending the User Model

```sql
DROP DATABASE storefront2;
CREATE DATABASE storefront2;
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Groups and Permissions

Create User - John Smith (Staff User)  
Create Customer - John Smith  
Create Auth Group - Customer Service (customer, order, order item)  
Relate John Smith <-> Customer Service  

# Securing APIs

## Token-based Authentication

A de facto standart for authenticating users with RESTful APIs

![Screenshot](./images/request.png?text=request)
![Screenshot](./images/response.png?text=response)

---

![Screenshot](./images/auth-request.png?text=auth-request)
![Screenshot](./images/auth-error-response.png?text=auth-error-response)
![Screenshot](./images/auth-token-response.png?text=auth-token-response)

TOKEN is temporary key we're going to give to the client to access protected resources

![Screenshot](./images/request-with-token.png?text=request-with-token)
![Screenshot](./images/auth-error-response.png?text=auth-error-response)
![Screenshot](./images/response-by-token.png?text=response-by-token)

## Adding the Authentication Endpoints

### Auth System
Models, tables, etc

### Djoser
Views for registration, login, etc

---

https://djoser.readthedocs.io/en/latest/authentication_backends.html  
### Auth Engines

 - Token-based Authentication
 - JSON Web Token Authentication

## Registering Users

Each component should have a <b>single responsibility</b>

## Logging In

http://127.0.0.1:8000/auth/jwt/create/  

JavaScript - Local Storage - Token

## Inspecting a JSON Web Token

https://www.jwt.io/

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzczNDAwNjE5LCJpYXQiOjE3NzM0MDAzMTksImp0aSI6IjE4MDRkZjVjMGQyOTRkM2FhOTE1YTI0ODFhYzg3ZjFiIiwidXNlcl9pZCI6IjMifQ.kOoLu7vtnkLQAPMaAi-utnQz6R7G38FIIM3HM3GHrow`

Decoded Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Decoded Payload
```json
{
  "token_type": "access",
  "exp": 1773400619,
  "iat": 1773400319,
  "jti": "1804df5c0d294d3aa915a2481ac87f1b",
  "user_id": "3"
}
```

Signature Verification  
`a-string-secret-at-least-256-bits-long`

## Refreshing Tokens

![Screenshot](./images/rt-request-token.png?text=rt-request-token)
![Screenshot](./images/unauthorized.png?text=unauthorized)
![Screenshot](./images/rt-request-refresh-token.png?text=rt-request-refresh-token)
![Screenshot](./images/response-access-token.png?text=response-access-token)

http://127.0.0.1:8000/auth/jwt/refresh/  
