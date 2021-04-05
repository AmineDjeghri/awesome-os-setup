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


Puis lancer jupyter lab sur la machine à distance avec, executez `jupyter notebook` sur le terminal ceci vous donnera une adresse avec un token, copiez la sur votre navigateur de votre pc personnel et vous aurez accès à la machine à distance
- Si vous voulez utiliser l'environnement du prof:  
 faire : source /users/nfs/Enseignants/piwowarski/venv/3.7/amal/bin/activate pour avoir l’environnement de AMAL si vous n’avez pas les trucs installés sur votre environnement  

Biensur vérifier les ports dans la machine à distance, si jupyter se lance sur un autre port, il faut que le ssh avec les ports correspond à celui de jupyter, 
Exemple : si jupyter est lancé sur le port 8899 et que votre ssh est sur le port 8888, ça ne marchera pas, il faut le meme port 
n’oubliez pas de fermer jupyter si vous avez perdu votre conx et que vous n’avez pas fermer la session, sinon il va se lancer sur un autre port
-	jupyter notebook list
-	jupyter notebook stop 8888

En plus du /tmp, vous avez également un répertoire /tempory qui est semi-permanent (n’est pas nettoyé à chaque reboot, mais plus rarement) de plus de 300Go, dans lequel vous pouvez travailler quand vous avez besoin de place.

#### Pour utiliser github :
Sur les machines à distance et pour pouvoir cloner un répo, saisir dans le terminal:

- `git config --global http.proxy http://proxy.ufr-info-p6.jussieu.fr:3128`
- `git config --global https.proxy https://proxy.ufr-info-p6.jussieu.fr:3128`

#### Pour installer des packages avec pip :  
faire  à chaque fois pour ma part dans le terminal les deux commandes:

export http_proxy=proxy:3128  
export https_proxy=proxy:3128  
Faire la commande : 
pip install -r http://webia.lip6.fr/~bpiwowar/requirements-amal.txt

- pour upgrade torch, il faut supprimer manuellement avec ncdu, le package torch dans .lib car torch demande énormément d'esapce pour etre mis à jour et ça dépassera le quota

#### pour le quota :
ncdu 
vider le .cache avec la lettre d

-	Vous pouvez utilisez jupyter notebook pour créer des fichiers txt, utiliser le terminal et visualiser vos documents
too old :
https://www-ppti.ufr-info-p6.jussieu.fr/index.php/faq/technique#pip-tme



### Need to add a new version with the support of pycharm and auto deploy :
Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save action. The difference between these two choices is explained in the field description.

[PPTI Official doc](https://www-ppti.ufr-info-p6.jussieu.fr/index.php/support/connexions-distantes)
https://www-ppti.ufr-info-p6.jussieu.fr/images/doc/connexions-windows.pdf
