# Smartdoor Host Web Application

A Django web application to manage NFC keys for smartdoor cliant.

![Smartdoor Host Web Home Page](docs/images/homepage.png)
*Caption: This website's Homepage, where the administrator can see and manage the list of user's keys.*


This repository includes `Dockerfile` and `docker-compose.yaml` files so that you can easily setup the web application in a docker container.
The instruction to deploy is given as follows.


## 1. Set environmental values

Before starting docker containers, you need to write environmental values in `.env` file. The following script is the example to write in `.env` file.
```bash
# === PostgreSQL ==========================================
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres


# === Django app ==========================================
# Database process name
DATABASE=postgres

# database connection settings
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# basic settings
ALLOWED_HOSTS=127.0.0.1,localhost

DJANGO_SECRET_KEY=XXX

CSRF_TRUSTED_ORIGINS=http://127.0.0.1,http://localhost


# === SSL/TLS setting =========================================================
CA_SUBJECT=NFC-key-ca
CA_EXPIRE=3600
SSL_EXPIRE=3600
SSL_SUBJECT=localhost
SSL_DNS=localhost

```
`CSRF_TRUSTED_ORIGINS` must contain the host server's address.

The `.env` file must be placed in the same directory where `Dockerfile` is located.


## 2. Create Login User

After starting up the container with the following command for the first time:

```bash
docker compose up -d
```
you need to set the login username and password.

Attach to the running docker container:
```shell
docker exec -it gunicorn-django bash
```
and excute the `creatingsuperuser` command:
```bash
python manage.py createsuperuser
```
Please refer to [how to create admin user](https://docs.djangoproject.com/en/4.0/intro/tutorial02/#creating-an-admin-user).

After setting username and password, you can access the login page (https://localhost/login/) and input username/passward.

![Smartdoor Host login](docs/images/loginpage.png)
*Caption: Login page*

**NOTE**
- When starting up containers, SSL certificates are automatically generated in ``ssl_certs`` directory. You can use CA certs there named as ``ca.pem`` if you would like to access webpage without any security warning.


## 3. Register NFC Key's IDm

When registering the NFC keys in this system, access the registration page by pushing the `Registration` button on the upper navigation bar, and fill in the form. The IDm information associated with each NFC device can manually input by keyboard or scanning an NFC tag with a NFC reader.

![Smartdoor Host registration](docs/images/keyregistration.gif)
*Caption: Demonstration of the NFC key registration.*

The system of reading an NFC tag's IDm is based on [SDK for NFC Web client](https://www.sony.co.jp/Products/felica/business/products/sdk/ICS-DCWC1.html) offered by SONY. Please check out the requirements to use this SDK, recommended NFC readers, etc.

---

## Launch development server

You can lauch the local server which Django offers.
Moving into the `smartdoor_prj` directory, and excute the following command:
```bash
python manage.py runserver --settings=smartdoor_prj.settings_dev
```
Then, the webpage will be available by accessing the http://localhost:8000.

`settings_dev.py` is a setting file written about Django configurations for development.


## Authenticate an IDm for Smartdoor client with the web API

In order for a smartdoor client to authenticate an detected IDm, this web sever offers the useful WebAPIs.
Access the keymanagement host address adding the `authenticate` endpoint (like http://\<host ip address\>/authenticate/),
and send the IDm in the following json format using html POST method:
```json
{"idm": "xxxaaayyyzzz"}
```

Before sending the above json data, it is required to obtain the CSRF token with html GET methd and apply it to the POST html header.

If the IDm is authenticated, the following json data is responsed:
```json
{
    "auth": "valid",
    "name": "Name",
    "allow_423": true,
    "allow_475": false,
}
```
`"Name"` means registerd user name in the host server. `"Allow_xxx"` means the allowed room number.

if not authenticated,
```json
{
    "auth": "invalid",
}
```

Smartdoor client app is been developped [here](https://github.com/munechika-koyo/smartdoor). You can install and use it as a smartdoor client.
