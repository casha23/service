# Service

## Installation

1. Clone repository

```console
foo@bar:~$ git clone https://github.com/casha23/service.git
```

2. Open project dir

```console
foo@bar:~$ cd service
```

3. Create and run virtualenv

4. Install requirements

```console
foo@bar:~/service$ pip install requirements.txt
```

5. Database setup

```console
foo@bar:~/service$ sudo -u postgres psql
CREATE DATABASE service_centre;
CREATE USER service_centre_user WITH PASSWORD '123456789';
ALTER USER service_centre_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE service_centre TO service_centre_user;
\q

```

6. Migrate

```console
foo@bar:~/service$ ./manage.py migrate
```

7. Create superuser

```console
foo@bar:~/service$ ./manage.py createsuperuser
```

8. Create master

```console
foo@bar:~/service$ ./manage.py create_master <phone_number> <password>
```

9. Runserver

```console
foo@bar:~/service$ ./manage.py runserver
```

Command for change Invoice status from Unpaid to Paid-up

```console
foo@bar:~/service$ ./manage.py pay_for_invoice <invoice_id>
```

## Testing

Run pytest

```console
foo@bar:~/service$ pytest
```
