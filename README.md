Smartdoor Host Web Application
===

A Django web application to manage NFC keys for smartdoor cliant.

This repository includes `Dockerfile` and `docker-compose.yaml` files so that you can easily setup web application in a docker container.


Create Login User
---
After starting up the container with the following command for the first time:

```Shell
docker-compose up -d
```
you will need to set the login username and password.

In this case, atach the running docker container:
```Shell
docker exec -it gunicorn-django bash
```
and excute the creating superuser command:
```Shell
python manage.py createsuperuser
```
Please refer to [how to create admin user](https://docs.djangoproject.com/en/4.0/intro/tutorial02/#creating-an-admin-user).

After setting username and password, you can access the login page (http://localhost:8000/login/) and pass through here.


Register NFC Key
---
The reading system of the IDm associating with NFC tag is based on [SDK for NFC Web client](https://www.sony.co.jp/Products/felica/business/products/sdk/ICS-DCWC1.html) which offered by Sony. Please check out the requirements for using this SDK like recommended NFC readers.