# How to use pycharm to run your code on PPTI GPU:
Open terminal: 
`ssh -L 6000:ppti-14-502-03.ufr-info-p6.jussieu.fr:22 LOGIN@ssh.ufr-info-p6.jussieu.fr`
Keep this terminal open 

Open Pycharm:

SSH Server: 
- login: same login 
- port: 6000 
- Host: localhost 

Deployment: 
- root: /tempory 
- project path : name project

pyhton interpreter : 
- same ssh config
- python interpreter path: /usr/bin/python3
- name: PPTI env
