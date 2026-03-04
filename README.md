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

## Resolving Circular Relationships

CIRCULAR DEPENDENCY

![Screenshot](./images/circular-relationship.png?text=circular-relationship)

# Setting Up the Database

## Supported Database Engines

### Database engines

- SQLite
- PostgreSQL
- MySQL
- MariaDB
- Oracle
- MS SQL Server

## Creating Migrations

```bash
python manage.py makemigrations
```

```bash
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py makemigrations
Was product.price renamed to product.unit_price (a DecimalField)? [y/N] y
Migrations for 'store':
  store/migrations/0002_rename_price_product_unit_price.py
    - Rename field price on product to unit_price
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ 
```

```bash
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py makemigrations
No changes detected
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ 
```

```bash
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py makemigrations
It is impossible to add a non-nullable field 'slug' to product without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 2
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py makemigrations
It is impossible to add a non-nullable field 'slug' to product without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> '-'
Migrations for 'store':
  store/migrations/0003_product_slug.py
    - Add field slug to product
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ 
```

## Running Migrations

```bash
python manage.py migrate
```

```bash
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, likes, store, tags
Running migrations:
  No migrations to apply.
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ 
```

```bash
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py sqlmigrate store 0003
BEGIN;
--
-- Add field slug to product
--
CREATE TABLE "new__store_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(50) NOT NULL, "title" varchar(255) NOT NULL, "description" text NOT NULL, "inventory" integer NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "collection_id" bigint NOT NULL REFERENCES "store_collection" ("id") DEFERRABLE INITIALLY DEFERRED, "unit_price" decimal NOT NULL);
INSERT INTO "new__store_product" ("id", "title", "description", "inventory", "created_at", "updated_at", "collection_id", "unit_price", "slug") SELECT "id", "title", "description", "inventory", "created_at", "updated_at", "collection_id", "unit_price", '-' FROM "store_product";
DROP TABLE "store_product";
ALTER TABLE "new__store_product" RENAME TO "store_product";
CREATE INDEX "store_product_slug_6de8ee4b" ON "store_product" ("slug");
CREATE INDEX "store_product_collection_id_2914d2ba" ON "store_product" ("collection_id");
COMMIT;
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ 
```

sequel - sql

## Reverting Migrations

```bash
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ python manage.py migrate store 0004
Operations to perform:
  Target specific migration: 0004_address_zip_code, from store
Running migrations:
  Rendering model states... DONE
  Unapplying store.0005_customer_store_custo_last_na_e6a359_idx_and_more... OK
(.venv) rovshen@rovshen:~/PyCharmProjects/django-practice$ 
```

## Installing PostgreSQL

[Download PostgreSQL](https://www.postgresql.org/download/)
