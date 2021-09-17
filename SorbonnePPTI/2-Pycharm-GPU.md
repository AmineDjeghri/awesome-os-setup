# How to use pycharm to run your code on PPTI :
JetBrains privides students a free Pycharm licence ! you can get one here : https://www.jetbrains.com/fr-fr/community/education/#students
Open terminal: 
`ssh -L 6000:ppti-14-407-03.ufr-info-p6.jussieu.fr:22 LOGIN@ssh.ufr-info-p6.jussieu.fr`
Replace LOGIN by your student number and Keep the terminal open (You can also change the number of the room (502-03)
This command will connect pycharm  to the PPTI machine. It will forward the output of the PPTI machine to the 6000 port of your computer, and pycharm will use this port to receive that output.

Open Pycharm: File ->settings->build, execution, deployment ->
If you don't know how to configure an ssh remote project on pycharm, follow this link https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html

settings of pycharm: 
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
