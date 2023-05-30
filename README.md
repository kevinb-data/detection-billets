# Bienvenue 

__Ceci est mon dossier repository retraçant le travail effectué sur mon projet de détection de faux billets pour l'ONCFM (Organisation Nationale de Lutte Contre le Faux-Monnayage)__

Le sujet était d'arriver à détecter des faux billets en python, avec un pourcentage de probabilité pour chaque billet.

Je disposais uniquement d'un jeu de données de 1500 lignes avec les variables suivantes :

- diagonal : la diagonale du billet

- height_left : la hauteur gauche du billet

- height_right : la hauteur droite du billet

- margin_low : la marge basse du billet

- margin_up : la marge haute du billet

- is_genuine : True ou False pour nous indiquer si les billets sont faux ou vrais.

__________________________________________________________________________________________________________

De ce jeu, nous devons construire un modèle de machine learning adéquat afin de détecter la véracité d'un billet donné hors de ce jeu initial.

J'ai donc développé un script en python qui a plusieurs résultats : 
- un modèle de regression logistique afin de prédire la valeur du billet (Vrai ou Faux) en fonction des différentes variables à disposition.
- un csv avec les prédictions
- un jeu de données final utilisé en fonction de si oui ou non une regression linéaire a été appliquée afin de combler les cellules vides qui pourraient se trouver au sein de la variable margin_low

J'ai également développé à la suite de ce script une web app grâce à streamlit, via jupyter notebook

__________________________________________________________________________________________________________

Les différentes sources de données produites durant ce projet sont présentes sous 'Source' dans ce dépôt.

Les différentes parties de code produites durant ce projet sont présentes sous 'Code' dans ce dépôt.

Afin de vous permettre de tester la web app vous-même, vous pouvez à n'importe quel moment y accéder via ce lien :

##########################################################################

 https://kevinb-data-detection-billets-web-app-v2-c3vj01.streamlit.app/
 
##########################################################################

__________________________________________________________________________________________________________

Il vous faudra également y déposer le fichier 'dataframe_final_20230530.csv' présent dans le dossier 'Sources' de ce dépôt ainsi que le modèle nommé 'modele_regression.joblib' présent dans le dossier 'Code' de ce dépôt.

Grâce au modèle de prédiction et à la web application, vous pourrez alors utiliser les boutons à disposition afin d'être en mesure de découvrir si votre billet, en fonction des valeurs en entrée que vous lui avez imputées, est vrai ou faux
