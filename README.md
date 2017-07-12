# touch-helsinki

Web portal for storing metal bar movement deltas and showing them in a browser.

## Prerequisites

* PostgreSQL (>= 9.3)
* Python (>= 3.4)

## Installation

### Database

touch-helsinki runs on PostgreSQL. Install the server on Debian-based systems with:

```bash
sudo apt install postgresql
```

Then create a database user and the database itself as the `postgres` system user:

```bash
createuser <your username>
createdb -l fi_FI.UTF8 -E UTF8 -T template0 -O <your username> touch_helsinki
```

### Code

Clone the repo:
```
git clone https://github.com/brains-on-art/touch-helsinki-web
cd touch_helsinki
```

Initiate a virtualenv and install the Python requirements:
```
pyenv virtualenv touch_helsinki-env
pyenv local touch_helsinki-env
pip install -r requirements.txt
```

Create `local_settings.py` in the repo base dir containing the following line:
```
DEBUG = True
```

Run migrations:
```
python manage.py migrate
```

Create admin user:
```
python manage.py createsuperuser
```

Run dev server:
```
python manage.py runserver
```
and open your browser to http://127.0.0.1:8000/admin/ using the admin user credentials.

## Misc. installation notes (preparing a blank EC2 Ubuntu 16.04 instance)

```
sudoedit /etc/locale.gen
    -> fi_FI.UTF-8
sudo locale-gen

sudo apt-get install postgresql
sudo -u postgres createuser touch_helsinki
sudo -u postgres createdb -l fi_FI.UTF8 -E UTF8 -T template0 -O touch_helsinki touch_helsinki
echo "ALTER USER touch_helsinki WITH PASSWORD 'touch_helsinki';" | sudo -u postgres psql


sudo apt-get install git python-pip virtualenv

pip install cookiecutter
pip install pip-tools

git clone https://github.com/brains-on-art/touch-helsinki-web
cd touch-helsinki-web

export LC_ALL=C.UTF-8
virtualenv -p python3 env
```
