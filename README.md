
## Initialisation 

Installer la librairie pandas
`pip install pandas`

Installer la librairie openpyxl
`pip install openpyxl`

Installer la librairie maptplot
`pip install matplotlib`

Lancer le fichier avec les données de "propre"
`python data.py`

Lancer le fichier avec les données de "propre" et "sales" qui ont été corrigées
`python data-error.py`

Questions du sujet : 

# Recommencez avec le jeu SI-erreur après avoir corrigé les valeurs en erreur. Précisez vos méthodes.
Nous avons décidé qu'une valeur était incorrecte si elle avait 15 degrés d'équart absolus avec le jour précédent ou le jour suivant.
Lorsqu'une valeur était en erreur ou incorrecte nous avons fait une moyenne entre le jour d'avant et le jour suivant. Si le jour suivant est aussi en erreur ou incorrecte nous avons pris celui d'après.

# Les données corrigées sont elles proches des valeurs sans erreur ?
Selon les courbes  les données que nous avons corrigés sont très proches des valeurs sans erreurs.

# A partir de données opendata du second fichier, retrouver le type de climat
Nous avons affaire à un pays du nord. C'est donc un climat dit "froid".

# Reprendre les données typiques de la localisation proche fournies en complément , comparer les écarts. Qu'en concluez vous ?
Les données fournies en complément n'ont pas l'air de se rapprocher avec nos données de base, les écarts sont trop importants.
Les moyennes de températures par mois de "Savukoski kirkonkyla" sont bien trop inférieures à celle du jeu de données fourni.

# De quelle la capitale européenne avez vous eu les données 
Il semblerait que la capitale soit Helsinki, la capitale de la Finlande !