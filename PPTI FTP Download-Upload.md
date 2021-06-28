## Graphic Acces to PPTI Sorbonne Université with FileZilla (download, upload, drag and drop files, rename, and more ...Ect) 

- Download filezilla without manuel, https://filezilla-project.org/download.php , 
- Open filezilla
- In host copy this adress: `ssh.ufr-info-p6.jussieu.fr`, 
- in username: your student number, 
- password: your student password, 
- in port: `22` (it is important to not leave this port empty)
- Left panels are your pc folders, right panels are the remote folders and files
- Drag and drop, rename, CTRL + A to select all and more ! Enjoy !

<img src="Azure steps/PPTI-FileZilla steps/filezilla ppti-part 1 .png" >
<img src="Azure steps/PPTI-FileZilla steps/filezilla ppti-part 2 .png" >




## Accès Machines Salle 407 et 502:
- Use this command for port forwarding in a terminal `ssh -L 6000:ppti-14-502-03.ufr-info-p6.jussieu.fr:22 LOGIN@ssh.ufr-info-p6.jussieu.fr
` 
- Change the login with yoru student number, and enter your password
- Open Filezilla and configure a new connection with: 
username: student number, password: your password, port: 6000, host: localhost, and change also the protocole to : SFTP SSH ...Ect

now you can browse the folders manually and even find the files of the /tempory folder, or use the search bar and search `/tempory`
