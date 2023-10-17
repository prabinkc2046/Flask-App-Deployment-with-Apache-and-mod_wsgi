# Flask App Deployment with Apache and mod_wsgi
This guide demonstrates how to deploy a simple Flask application using Apache as the front-end web server and mod_wsgi as the bridge between Apache and the Flask application. This setup allows Apache to handle incoming requests, recognize URLs, and forward them to the Flask application.

# Prerequisites
1. Ubuntu operating system
2. sudo access
3. Basic knowledge of Python and Flask

# Build a Simple Flask Application

## Update and Upgrade Ubuntu:

```bash
sudo apt update
sudo apt upgrade
```

## Install Python and Virtual Environment:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

## Create a Project Directory:

```bash
sudo mkdir /var/www/hello-world
sudo chown -R $USER:$USER /var/www/hello-world
cd /var/www/hello-world
```

## Create a Simple Flask Application:
Save the following code as app.py:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
```

## Create a Virtual Environment and Run the Flask App:

```bash
python3 -m venv venv
source venv/bin/activate
pip install Flask
python app.py
```

The app should be accessible at http://localhost:5000.

# Configure Apache and mod_wsgi
Install Required Packages:

```bash
sudo apt install apache2 libapache2-mod-wsgi-py3
```

## Create a WSGI Script:

```bash
sudo nano /var/www/hello-world/hello-world.wsgi
```
## Add the following content:

```python
import sys

sys.path.insert(0, '/var/www/hello-world')
sys.path.insert(0, '/var/www/hello-world/venv/lib/python3.10/site-packages/')

from app import app as application
```
Save the file.

## Configure Apache Virtual Host:

```bash
sudo nano /etc/apache2/sites-available/hello-world.conf
```

Add the following content:

```apache
<VirtualHost *:80>
    ServerName  <serverIP or domain name>
    ServerAdmin webmaster@localhost
    WSGIDaemonProcess hello-world threads=5
    WSGIScriptAlias / /var/www/hello-world/hello-world.wsgi
    <Directory hello-world>
         WSGIProcessGroup hello-world
         WSGIApplicationGroup %{GLOBAL}
         Order deny,allow
         Allow from all
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/hello-world-error.log
    CustomLog ${APACHE_LOG_DIR}/hello-world-access.log combined
</VirtualHost>
```
Save the file.

Enable the Configuration:

```bash
sudo a2ensite hello-world.conf
```
Restart Apache:

```bash
sudo systemctl restart apache2
```
Now, the Flask app can be accessed at http://server_ip. This setup uses Apache as the front-end server, forwarding requests to the Flask application running in the background.





