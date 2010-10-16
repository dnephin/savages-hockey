#!/bin/bash
# deploy in production


cp -r hockey_register ~
cp ./conf/settings.py-prod ~/hockey_register/settings.py
mkdir  ~/hockey_register/public
cp ./prod/* ~/hockey_register/public
cp ./prod/.htaccess ~/hockey_register/public
ln -s /usr/local/alwaysdata/python/django/1.1/django/contrib/admin/media/ ~/hockey_register/public/admin-media 

