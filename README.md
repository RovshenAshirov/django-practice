# The Ultimate Django Series: Part 3

required: Python 3.12 version

## Setting Up the Project

```sql
CREATE DATABASE storefront3
```

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_db
python manage.py createsuperuser
```

# Uploading Files

## Setting Up the Client App

required: Node 17 version

```bash
node --version
cd client_app
npm install
npm start
```

## Enabling CORS

CORS - Cross-origin Resource Sharing

http://domain1.com  
http://domain2.com
