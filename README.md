
------------------------------------------------------------------------------------------------------
PROJET ARCHITECTURE SI
------------------------------------------------------------------------------------------------------
Quelles sont les notions qui vont être abordées au cours de cet atelier ?
Cet atelier a pour objectif de vous apprendre à créer des bases de données grace à Python et SQLite. Vous allez ensuite exploter cette base de données via la construction d'API. Vous allez utiliser et mettre en oeuvre au travers de cet atelier, un serveur Python utilisant le Framework Flask. 
Vous allez créer des API, découvrir les Actions et les Secrets GitHUB pour au final mettre en service et exploiter une base de données.
Large programme mais tout à fait accessible et ne nécessitant pas de base technique particulière. Juste de l'observation et de la rigueur dans votre travail. 

-------------------------------------------------------------------------------------------------------
Séquence 1 : GitHUB
-------------------------------------------------------------------------------------------------------
Objectif : Création d'un Repository GitHUB pour travailler avec son projet  
Difficulté : Très facile (~10 minutes)
-------------------------------------------------------------------------------------------------------
GitHUB est une plateforme en ligne utilisée pour stocker le code de son programme.
GitHUB est organisé en "Repository", c'est à dire en répertoire (contenant lui même des sous répertoires et des fichiers). Chaque Repository sera indépendant les un des autres. Un Repository doit être vu comme un projet unique (1 Repository = 1 Projet). GitHUB est une plateforme très utilisée par les informaticiens.

**Procedure à suivre :**  
1° - Créez vous un compte sur GitHub : https://github.com/  
Si besoin, une vidéo pour vous aider à créer votre propre compte GitHUB : [Créer un compte GitHUB](https://docs.github.com/fr/get-started/onboarding/getting-started-with-your-github-account)  
A noter que **si vous possédez déjà un compte GitHUB, vous pouvez le conserver pour réaliser cet atelier**. Pas besion d'en créer un nouveau.  
Remarque importante : **Lors de votre inscription, utilisez une adresse mail valide. GitHUB n'accepte pas les adresses mails temporaires**  

2° - Faites un Fork du Repository suivant : [https://github.com/OpenRSI/Flask_Projet_SQLite](https://github.com/OpenRSI/Flask_Projet_SQLite)  
Voici une vidéo d'accompagnement pour vous aider dans les "Forks" : [Forker ce projet](https://youtu.be/p33-7XQ29zQ)    
  
**Travail demandé :** Créé votre compte GitHUB, faites le fork de ce projet et **copier l'URL de votre Repository GitHUB dans la discussion public**.

Notion acquise lors de cette séquence :  
Vous avez appris lors de cette séquence à créer des Repository pour stocker et travailler avec votre code informatique. Vous pourez par la suite travailler en groupe sur un projet. Vous avez également appris à faire des Forks. C'est à dire, faire des copies de projets déjà existant dans GitHUB que vous pourrez ensuite adapter à vos besoins.
  
---------------------------------------------------
Séquence 2 : Création d'un hébergement en ligne
---------------------------------------------------
Objectif : Créer un hébergement sur Alawaysdata  
Difficulté : Faible (~10 minutes)
---------------------------------------------------

Rendez-vous sur **https://www.alwaysdata.com/fr/**  
  
Remarque : **Attention à bien vous rappeler de vos Login/Password** lors de la création de votre compte site car vous en aurez besoin plus tard pour la création de vos Secrets GitHUB.  
  
Voici une vidéo d'accompagnement pour vous aider dans cette séquence de création d'un site sur Alwaysdata : [Vidéo Alwaysdata](https://youtu.be/6cuHjy8n968)  
  
**Procédure :**  
Conservez votre site Alwaysdata existant (sous Flask).  
    
**Travail demandé :** Mettre en ligne votre application Flask "Hello World !" et **copier l'URL de votre site dans la discussion public**.  
  
Notions acquises lors de cette séquence :  
Vous avez créer un hébergement (gratuit) et découvert également que vous pouvez installer bien d'autres applications (Django, Drupal, Jenkins, Magento, Symphony, etc...). Les perspectives sont nombreuses.

---------------------------------------------------------------------------------------------
Séquence 3 : Les Actions GitHUB (Industrialisation Continue)
---------------------------------------------------------------------------------------------
Objectif : Automatiser la mise à jour de votre hébergement Alwaysdata  
Difficulté : Moyenne (~15 minutes)
---------------------------------------------------------------------------------------------
Dans le Repository GitHUB que vous venez de créer précédemment lors de la séquence 1, vous avez un fichier intitulé CICD.yml et qui est déposé dans le répertoire .github/workflows. Ce fichier a pour objectif d'automatiser le déploiement de votre code sur votre site Alwaysdata. Pour information, c'est ce que l'on appel des Actions GitHUB. Ce sont des scripts qui s'exécutent automatiquement lors de chaque Commit dans votre projet (C'est à dire à chaque modification de votre code). Ces scripts (appelés actions) sont au format yml qui est un format structuré proche de celui d'XML.  

Pour utiliser cette Action (CICD.yml), **vous avez besoin de créer des secrets dans GitHUB** afin de ne pas divulguer des informations sensibles aux internautes de passage dans votre Repository comme vos login et password par exemple.  

Pour ce projet Métriques, **vous avez 4 secrets à créer** dans votre Repository GitHUB :  
**USERNAME** = Le login qui est utilisé pour la connexion SSH.  
**PASSWORD** = Le mot de passe qui est utilisé pour la connexion SSH.  
**ALWAYSDATA_TOKEN** = Le token est à créer depuis l'interface d'administration Alwaysdata. Cliquez sur votre profil en haut à droite, puis sur 'Profil' puis sur 'Gérer les tokens'. Laissez le champ "Adresses IP autorisées" vide. Dans le cas contraire vous limiteriez les connexions seulement à une adresse IP. Pour le champ Application* mettez "Monprojet" par exemple.  
**ALWAYSDATA_SITE_ID** = Vous trouverez l'ID de votre site depuis l'interface d'administration Alwaysdata dans les paramètres de votre site, c'est à dire la petite roue crantée à "droite" puis dans le titre #XXXXX. XXXXX étant l'ID de votre site. Ne prenez pas le # mais juste les chiffres.  
  
Voici une vidéo pour vous expliquer le processus de création de vos secrets dans GitHUB : [Création des secrets](https://youtu.be/pi80zRdrJyQ)  
Vous pouvez à présent **lancer une action pour mettre en ligne votre solution**.  

**Dernière étape :** Pour engager l'automatisation de votre première Action, vous devez cliquer sur le gros boutton vert dans l'onglet supérieur Actions. Le boutton s'intitule "I understand my workflows, go ahead and enable them"  
  
![Screenshot Actions](Actions_Button.jpg)   

Notions acquises de cette séquence :  
Vous avez vu dans cette séquence comment créer des secrets GiHUB afin de mettre en place de l'industrialisation continue.  
L'utilité des scripts d'actions (C'est à dire des scripts exécutés lors des Commits) est très importante mais sortes malheureusement du cadre de cet atelier faute de temps. Toutefois, je vous invites à découvrir cet outil via les différentes sources du Web (Google, ChatGPT, etc..).  

---------------------------------------------------
Séquence 4 : Créer la base de données sur votre serveur
---------------------------------------------------
Objectif : Créer la base de données SQLite sur votre serveur  
Difficulté : Faible (~10 minutes)
---------------------------------------------------
1° - Connectez vous en SSH à votre serveur Alwaysdata via l'adresse suivante :**https://ssh-{compte}.alwaysdata.net**. Remarque importante, {compte] est à remplacer par votre compte Alwaysdata. C'est à dire le compte que vous avez utilisé pour renseigner votre secret GitHUB USERNAME.   
2° - Une fois connecté, depuis de la console SSH, executez la commande suivante : **cd www/flask** puis **python3 create_db.py**  
Votre base de données est à présent opérationnelle sur votre serveur (Le fichier database.db à été créé dans votre répertoire sur le serveur)
Vous pouvez, si vous le souhaitez, tappez la commande **ls** dans votre console pour voir la présence de la base de données.

LES ROUTES (API)
-------------------------------------------
Votre solution est à présent opérationnelle. Vous pouvez testez les routes (API) comme suit :  
  
https://{Votre_URL}**/**  
Pointe sur le fichier helloWorld d'accueil  

https://{Votre_URL}**/lecture**  
L'accès est conditionné à un contrôle d'accès  

https://{Votre_URL}**/authentification**  
Page d'authentification (admin, password)  

https://{Votre_URL}**/fiche_client/1**  
Permet de faire un filtre sur un client. Vous pouvez changer la valeur de 1 par le N° du client de votre choix  

https://{Votre_URL}**/consultation/**  
Permet de consutler la base de données  

https://{Votre_URL}**/enregistrer_client**  
API pour enregistrer un nouveau client  

---------------------------------------------------
Séquence 5 : Exercices
---------------------------------------------------
Objectif : Travailler votre code  
Difficulté : Moyenne (~60 minutes)
---------------------------------------------------
**Exercice 1 : Création d'une nouvelle fonctionnalité**    
Créer une nouvelle route dans votre application afin de faire une recherche sur la base du nom d'un client.  
Cette fonctionnalité sera accéssible via la route suivante : **/fiche_nom/**  

**Exercice 2 : Protection**  
Cette nouvelle route "/fiche_nom/" est soumise à un contrôle d'accès User. C'est à dire différent des login et mot de passe administrateur.  
Pour accéder à cette fonctionnalité, l'utilisateur sera authentifié sous les login et mot de passe suivant : **user/12345**
  
---------------------------------------------------
Séquence 6 : Le projet de bibliothèque
---------------------------------------------------
Objectif : Créer une application de biliothèque  
Difficulté : Moyenne (~3h)
---------------------------------------------------
Votre projet consiste à present à concevoir et développer une application de gestion de bibliothèque moderne qui simplifie le processus de prêt et de retour de livres. Les fonctionnalités attendues dans le cadre de ce projet sont les suivantes :  
•	L’enregistrement et la suppression de livres.  
•	La recherche de livres disponibles.  
•	L'emprunt possible d'un livre par un utilisateur.  
•	La gestion des utilisateurs.  
•	La gestion des stocks.  
Votre travail est de modifier votre code afin de répondre aux besoins définis ci-dessus.
L'application exploitera des API pour interagir avec la base de données et un contrôle d'accès Utilisateur/Administrateur doit être mis en place.  
L’application pourra être enrichie avec des fonctionnalités supplémentaires telles que des recommandations de livres, des notifications pour les retours en retard, ou encore des rapports statistiques sur l'utilisation des livres pour améliorer l'expérience utilisateur et la gestion de la bibliothèque.  

--------------------------------------------------------------------
Troubleshooting :
---------------------------------------------------
Objectif : Visualiser ses logs et découvrir ses erreurs
---------------------------------------------------
Lors de vos développements, vous serez peut-être confronté à des erreurs systèmes car vous avez faits des erreurs de syntaxes dans votre code, faits de mauvaises déclarations de fonctions, appelez des modules inexistants, mal renseigner vos secrets, etc…  
Les causes d'erreurs sont quasi illimitées. **Vous devez donc vous tourner vers les logs de votre système pour comprendre d'où vient le problème** :  
Voici une vidéo pour accéder aux logs de vos Actions GitHUB : [Vidéo Log GitHUB](https://youtu.be/rhGrDLSFH7Y)  
Voici une vidéo pour vous expliquer comment accéder au logs de votre serveur Alwaysdata : [Vidéo Log Alwaysdata](https://youtu.be/URWMWqVMS2U)  
  
