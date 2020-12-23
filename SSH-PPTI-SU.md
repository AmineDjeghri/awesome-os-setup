## Utiliser Jupyter notebook sur votre propre navigateur en ssh tunnel via les PCs de l'université (ppti) 

#### installer gitbash
#### Modifier le fichier .ssh/config 
- Il faut pour cela rajouter dans votre .ssh/config `cd .ssh` les lignes en bas et remplacer votre_login dans les deux blocs par votre numéro étudiant:  
exemple: User 23020202 (N'oubliez pas de le faire dans les deux blocs)

----------------------------------------------------
Host ppti  
User votre_login  
Hostname ssh.ufr-info-p6.jussieu.fr
<br/><br/>
Host *.ppti  
User votre_login  
ProxyCommand ssh ppti -W $(basename %h .ppti):%p  

----------------------------------------------------

#### Créer une clé shh d’abord `ssh-keygen -o`
documentation: https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key

#### Tester SSH
- Deux salles de la ppti sont équipées de bons GPUs : la 502 et la 407. Pour se connecter, en ssh en passant par la passerelle ssh.ufr-info-p6.jussieu.fr,  puis ppti-14-502-XX (XX=01 à 16) ou ppti-14-407-XX, saisir la commande dans gitbash: 

`ssh -L8888:localhost:8888 -L6006:localhost:6006 ppti-14-502-03.ppti` 
(j'ai mis deux ports au cas où, pour jupyter et tensorboard)  
Une fois connecté, il vous demandera votre mot de passe de votre compte étudiant, deux fois


- Avant chaque TME, penser à exécuter pip install -r http://webia.lip6.fr/~bpiwowar/requirements-amal.txt afin de profiter de l’environnement avec tous les modules installés. 
- Sur les machines de la ppti, l’environnement peut être activé en exécutant : source /users/nfs/Enseignants/piwowarski/venv/3.7/amal/bin/activate


Puis lancer jupyter lab sur la machine à distance avec, executez `jupyter notebook` ceci vous donnera une adresse avec un token, copiez la sur votre navigateur de votre pc personnel et vous aurez accès à la machine à distance
- Si vous voulez utiliser l'environnement du prof:  
 faire : source /users/nfs/Enseignants/piwowarski/venv/3.7/amal/bin/activate pour avoir l’environnement de AMAL si vous n’avez pas les trucs installés sur votre environnement  

Biensur vérifier les ports, si jupyter se lance sur un autre port, il faut que le ssh avec les ports correspond à celui de jupyter, n’oubliez pas de fermer jupyter si vous avez perdu votre conx et que vous n’avez pas fermer la session, sinon il va se lancer sur un autre port
-	jupyter notebook list
-	jupyter notebook stop 8888

En plus du /tmp, vous avez également un répertoire /tempory qui est semi-permanent (n’est pas nettoyé à chaque reboot, mais plus rarement) de plus de 300Go, dans lequel vous pouvez travailler quand vous avez besoin de place.

#### Pour utiliser github :
sur les machines à distance et pouvoir cloner un répo, il faut ajouter une clé ssh et ajouter  :  
ssh.ufr-info-p6.jussieu.fr  dans le fichier de git config si je me souviens bien

#### Pour installer des packages avec pip :
export http_proxy=proxy:3128
export https_proxy=proxy:3128
Faire la commande : 
pip install -r http://webia.lip6.fr/~bpiwowar/requirements-amal.txt

#### pour le quota :
ncdu 
vider le .cache avec la lettre d

-	Vous pouvez utilisez jupyter notebook pour créer des fichiers txt, utiliser le terminal et visualiser vos documents
too old :
https://www-ppti.ufr-info-p6.jussieu.fr/index.php/faq/technique#pip-tme
