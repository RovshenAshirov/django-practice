# The Ultimate Django Series: Part 1

## What is Django?

Free and open-source **framework** for building **web apps** with **Python**

LESS TIME. LESS CODE

### Companies Using Django

- YouTube
- Instagram
- Spotify
- DropBox

BATTERIES INCLUDED

### Django Features

- The admin site
- Object-relational mapper (ORM)
- Authentication
- Caching

JOHN SMITH

Programming brain genius

"DJANGO IS A PIECE OF CRAP!"

"It's old!"

"It's got too many features!"

PERFORMANCE ISN'T EVERYTHING

- Maturity
- Stability
- Difficulty
- Community

Django has a huge community

There's always someone to help you!

Django comes with a LOT of features...

But you don't have to use them all

Debates about "the best framework in the world" are USELESS!

Django Developer - $117,673/year - ziprecruiter.com

LEARNING DJANGO IS A GOOD INVESTMENT FOR YOUR FUTURE

## How to Web Works?

**Django** is a **framework** for building web applications

![Screenshot](./images/front-end_and_back-end.png?text=Front-end+and+Back-end)

moshbuy.com

URL - Uniform Resource Locator

`page` `image` `video` `pdf`

![Screenshot](./images/request.png?text=Request)


![Screenshot](./images/response.png?text=Response)

HTTP - Hypertext Transfer Protocol

![Screenshot](./images/html.png?text=HTML)

HTML - Hypertext Markup Language

![Screenshot](./images/data.png?text=DATA)

CLIENT

- REACT
- ANGULAR
- VUE

SERVER

- DJANGO
- ASP.NET CORE
- EXPRESS

![Screenshot](./images/endpoints.png?text=endpoints)

API - Application Programming Interface

![Screenshot](./images/structure.png?text=structure)

WE'RE READY TO SET UP OUR DEVELOPMENT

## Setting Up the Development Environment

```bash
python3 --version
```

python 3.9.5

```bash
pip3 install virtualenv
```

## Creating Your First Django Project

```bash
cd PycharmProjects
mkdir storefront
cd storefront
virtualenv venv
source venv/bin/activate
pip install Django==4.2.10
```

![Screenshot](./images/django-admin.png?text=Django-Admin)

```bash
ls
```

Open this folder in PyCharm Professional

```bash
django-admin
django-admin startproject storefront
django-admin startproject storefront .
django-admin runserver # error
python manage.py
python manage.py runserver    
python manage.py runserver 8000
```

Click [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Creating Your First App

![Screenshot](./images/apps.png?text=Apps)

```bash
python manage.py startapp playground
```

# Building a Data Model

## Introduction to Data Modeling

![Screenshot](./images/product-collection.png?text=model)

### Relationships

- One-to-one (1, 1)
- One-to-many (1, *)
- Many-to-many (*, *)

Idenify the other essential entities we need in an e-commerce application

Hint: 5 Entities

## Building an E-commerce Data Model

![Screenshot](./images/created_at.png?text=created_at)

![Screenshot](./images/association-class.png?text=association-class)

![Screenshot](./images/many-to-many.png?text=many-to-many)

What about the user that owns this cart?

![Screenshot](./images/e-commerce.png?text=e-commerce)

![Screenshot](./images/tag.png?text=tag)

## Organizing Models in Apps

### STORE

- Product
- Collection
- Cart
- CartItem
- Order
- OrderItem
- Customer

But there's a problem...

Monolith

Do one thing and do it well.

![Screenshot](./images/models-apps.png?text=models-apps)

![Screenshot](./images/model-app.png?text=model-app)

Takeaway

MINIMAL COUPLING
HIGH COHESION (FOCUS)

```bash
python manage.py startapp store
python manage.py startapp tags
```
