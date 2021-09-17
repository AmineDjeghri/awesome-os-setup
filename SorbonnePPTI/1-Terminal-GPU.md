# SSH to connect to the GPU machines of PPTI 

## TLDR; 
- use this command if you want to connect the GPUs rooms of the PPTI and change the LOGIN with your student number :

`ssh -L 8888:localhost:8888 -L 6006:localhost:6006  -J LOGIN@ssh.ufr-info-p6.jussieu.fr LOGIN@ppti-14-407-03.ufr-info-p6.jussieu.fr`
- enter two times the password 
- check if the gpu is available in the machines : nvidia-smi
- to change the room and machines : replace the YY and XX in ppti-14-YY-XX.ufr-info-p6.jussieu.fr , YY: 407 or 502, XX:01 to 10

## Explaination
### 1-Proxy Jump
To connect to the PPTI machines that have GPUs (407 and 502) you need to:
- first : connect to the PPTI gateway (ssh.ufr-info-p6.jussieu.fr)
- second : inside the ppti gateway, connect to the machines 

To do this we can connect to the gateweway, and from inside it connect to the machines, or we can do a proxy jump `-J` to directly connect to machines
`ssh -J user@<bastion:port> <user@remote:port>`

In our case it will be : `ssh -J LOGIN@ssh.ufr-info-p6.jussieu.fr LOGIN@ppti-14-407-03.ufr-info-p6.jussieu.fr`

### 2-Port forwarding 
We can jupyter notebooks and tensorboards on the remote machine, and forward the output to our local machine. 
- To do this, we just need to use the port forwading `-L` to forward the output of the app `ssh -L local_port:destination_server_ip:remote_port ssh_server_hostname`.
- So to use jupyternotebook in our machine will do `ssh -L 8888:localhost:8888 ssh_server_hostname` (localhost for our machine, 8888 because jupyter uses this as default but you can change it)
- In our case to use it with the PPTI machines `ssh -L 8888:localhost:8888 -J 3801757@ssh.ufr-info-p6.jussieu.fr 3801757@ppti-14-407-03.ufr-info-p6.jussieu.fr`
- For two apps (tensorboard and Jupyter notebook) : `ssh -L 8888:localhost:8888 -L 6006:localhost:6006  -J 3801757@ssh.ufr-info-p6.jussieu.fr 3801757@ppti-14-407-03.ufr-info-p6.jussieu.fr`
