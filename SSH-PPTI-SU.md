## Utiliser Jupyter notebook sur votre propre navigateur en ssh tunnel via les PCs de l'université (ppti) 

- installer gitbash
Il faut pour cela rajouter dans votre .ssh/config : 
`cd .ssh`
ou: 
`cd ` # pour aller à la racine
`ls -a` # Pour afficher , si .ssh n'existe pas, creer le avec `mkdir` creer le fichier config dedans

ajouter dans le fichier config ces lignes:

`

Host ppti

User votre_login

Hostname ssh.ufr-info-p6.jussieu.fr

Host *.ppti

User votre_login

ProxyCommand ssh ppti -W $(basename %h .ppti):%p
`


#### Créer une clé shh d’abord `ssh-keygen -o`
documentation: https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key


•  Avant chaque TME, penser à exécuter pip install -r http://webia.lip6.fr/~bpiwowar/requirements-amal.txt afin de profiter de l’environnement avec tous les modules installés. 
•  Sur les machines de la ppti, l’environnement peut être activé en exécutant : source /users/nfs/Enseignants/piwowarski/venv/3.7/amal/bin/activate
•  Deux salles de la ppti sont équipées de bons GPUs : la 502 et la 407. Pour se connecter, en ssh en passant par la passerelle ssh.ufr-info-p6.jussieu.fr,  puis ppti-14-502-XX (XX=01 à 16) ou ppti-14-407-XX. 


•  Vous pouvez lancer un jupyter lab a distance sur ces machines : 
faire ssh -L8888:localhost:8888 ppti-14-502-XX.ppti
Puis lancer jupyter lab sur la machine distance avec ‘jupyter notebook’ ceci vous donnera une adresse avec un token,
 copiez la sur votre navigateur de votre pc personnelle et vous aurez accès à la machine à dtistance
N’oubliez avant de faire ça de faire : source /users/nfs/Enseignants/piwowarski/venv/3.7/amal/bin/activate pour avoir l’environnement de AMAL si vous n’avez pas les trucs installés sur votre environnement
En local, vous utilisez l’adresse habituelle de jupyter, http://localhost:8888.
Biensur vérifier les ports, si jupyter se lance sur un autre port, il faut que le ssh avec les ports correspond à celui de jupyter, n’oubliez pas de fermer jupyter si vous avez perdu votre conx et que vous n’avez pas fermer la session, sinon il va se lancer sur un autre port
-	jupyter notebook list
-	jupyter notebook stop 8888
-	


En plus du /tmp, vous avez également un répertoire /tempory qui est semi-permanent (n’est pas nettoyé à chaque reboot, mais plus rarement) de plus de 300Go, dans lequel vous pouvez travailler quand vous avez besoin de place.

#### Pour utiliser github :
sur les machines à distance et pouvoir cloner un répo, il faut ajouter une clé ssh et ajouter  :  ssh.ufr-info-p6.jussieu.fr  dans le fichier de git config si je me souviens bien

#### Pour installer des packages avec pip :
export http_proxy=proxy:3128
export https_proxy=proxy:3128
Faire la commande : 
pip install -r http://webia.lip6.fr/~bpiwowar/requirements-amal.txt

#### pour le quota :
ncdu 
vider le .cache avec la lettre d

-	Vous pouvez utilisez jupyter notebook pour créer des fichiers txt, utiliser le termional et visualiser vos documents
too old :
https://www-ppti.ufr-info-p6.jussieu.fr/index.php/faq/technique#pip-tme
