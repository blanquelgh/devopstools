Hola Mundo.

docker login registry.cto1.paas.gsnetcloud.corp

root@kubernetes-VirtualBox:/opt/ngrok/workspacepython# docker tag python_bot_build:v1.0.2 registry.cto1.paas.gsnetcloud.corp/mxsre/python_bot_build:v1.0.2

root@kubernetes-VirtualBox:/opt/ngrok/workspacepython# docker push registry.cto1.paas.gsnetcloud.corp/mxsre/python_bot_build:v1.0.2
The push refers to a repository [registry.cto1.paas.gsnetcloud.corp/mxsre/python_bot_build]

root@kubernetes-VirtualBox:/opt/ngrok/workspacepython# docker push registry.cto1.paas.gsnetcloud.corp/mxsre/firejava:latest
The push refers to a repository [registry.cto1.paas.gsnetcloud.corp/mxsre/firejava]
An image does not exist locally with the tag: registry.cto1.paas.gsnetcloud.corp/mxsre/firejava
root@kubernetes-VirtualBox:/opt/ngrok/workspacepython# docker tag firejava:latest registry.cto1.paas.gsnetcloud.corp/mxsre/firejava:latest
root@kubernetes-VirtualBox:/opt/ngrok/workspacepython# docker push registry.cto1.paas.gsnetcloud.corp/mxsre/firejava:latest
The push refers to a repository [registry.cto1.paas.gsnetcloud.corp/mxsre/firejava]
ea89e593fdf8: Pushed 
bfb0613f8bab: Pushed 
5579456c06d9: Pushed 
eac26a81bf81: Pushed 
4d4fc9e087a4: Pushed 
ca306a4c45cf: Pushed 
b57c79f4a9f3: Mounted from mxsre/python_bot_build 
d60e01b37e74: Mounted from mxsre/python_bot_build 
e45cfbc98a50: Mounted from mxsre/python_bot_build 
762d8e1a6054: Mounted from mxsre/python_bot_build 
latest: digest: sha256:13515e5c7ddc28b87f43ca17bf91ec3b052112c2ac9c04402e09febc4c07325d size: 2406
root@kubernetes-VirtualBox:/opt/ngrok/workspacepython# 
