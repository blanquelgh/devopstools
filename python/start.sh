#!/bin/bash

cd /opt/bot
git init
git clone -b development ssh://git@gitlab.pro.pandora.mx.corp:2220/devopsmx/aot-proyectos/python-bot.git
cd /opt/bot/python-bot


pip3 install --upgrade pip3
/usr/bin/python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

cp initbotPOO.py /opt/bot/botpython/
chmod 755 /opt/bot/
chown py3:gpy3 /opt/bot/


su - py3
cd /opt/bot/botpython/
python3 initbotPOO.py -p 8080
