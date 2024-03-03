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