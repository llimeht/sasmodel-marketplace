#!/bin/sh

WSGIPATH="$(sudo find /usr/local/lib -name 'mod_wsgi*gnu.so')"

echo 'LoadModule mod_wsgi "'$WSGIPATH'"' | sudo tee /etc/apache2/mods-enabled/mod_wsgi.load
