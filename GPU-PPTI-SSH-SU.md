# How to use pycharm to run your code on PPTI GPU:
Open terminal: 
`ssh -L 6000:ppti-14-502-03.ufr-info-p6.jussieu.fr:22 LOGIN@ssh.ufr-info-p6.jussieu.fr`
Keep this terminal open 

Open Pycharm:

SSH Server: 
- login: same login 
- port: 6000 
- Host: localhost 
- changer le nom en: ssh ppti su

Deployment: 
- root: /tempory 
- project path : name project
- changer le nom: ssh-deploy

pyhton interpreter : 
- same ssh config
- python interpreter path: /usr/bin/python3
- name it: PPTI env


## Make the deployment the default one and in options check the `send when save`
## Use the new interpreter 
