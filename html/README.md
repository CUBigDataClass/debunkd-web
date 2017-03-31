## Instructions to deploy

#### Setup Systemd to start uWSGI

Setup the virtual environment:
```
$ virtualenv sbenv
```

Afterwards, install dependencies with the command:
```
$ pip install -r requirements.txt
```

Move the systemd Unit file to the correct directory:
```
$ mv sb-web.service /etc/systemd/system/
```

Now to start the uwsgi service, run the command:
```
$ sudo systemctl start sb-web
```

#### Configure nginx

Move files to their directories:
```
$ mv ngx_sbweb /etc/nginx/sites-available/
```

Set symlink to enable our nginx configuration
```
$ sudo ln -s /etc/nginx/sites-available/ngx_sbweb /etc/nginx/sites-enabled
```

Now restart nginx
```
$ sudo systemctl restart nginx
```

Now, you can visit the server IP to view the web application! Yay

