# How to use pycharm to run your code on PPTI with GPUs:
Open terminal: 
`ssh -L 6000:ppti-14-502-03.ufr-info-p6.jussieu.fr:22 LOGIN@ssh.ufr-info-p6.jussieu.fr`
Replace LOGIN by your student number and Keep the terminal open (You can also change the number of the room (502-03)

Open Pycharm:

SSH Server: 
- login: LOGIN
- port: 6000 
- Host: localhost 
- changer le nom en: ssh ppti su

Deployment: 
- root: /tempory 
- project path : name project
- change the name le nom: ssh-deploy

Pyhton interpreter: 
- same ssh config
- python interpreter path: /usr/bin/python3
- name it: PPTI env


## Make the deployment the default one and in options check the `send when save`
## Use the new interpreter 
