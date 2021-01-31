
## Initialisation 

Installer la librairie pandas
`pip install pandas`

Installer la librairie openpyxl
`pip install openpyxl`

Installer la librairie maptplot
`pip install matplotlib`

Lancer le fichier 
`python data.py`

# If the absolute difference between next day and previous day is > 15°C then it's considered as an error
            # We check values and the average difference is 15°C expect for records.
Questions du sujet : 

# Recommencez avec le jeu SI-erreur après avoir corrigé les valeurs en erreur. Précisez vos méthodes.
Nous avons décidé qu'une valeur était incorrecte si elle avait 15 degrés d'équart avec le jour précédent ou le jour suivant.
Lorsqu'une valeur était en erreur ou incorrecte nous avons fait une moyenne entre le jour d'avant et le jour suivant. Si le jour suivant est aussi en erreur ou incorrecte nous avons pris celui d'après.

# Les données corrigées sont elles proches des valeurs sans erreur ?
Selon les courbes  les données que nous avons corrigés sont très proches des valeurs sans erreurs.

# A partir de données opendata du second fichier, retrouver le type de climat
Nous avons affaire à un pays du nord. C'est donc un climat dit "froid".

# Reprendre les données typiques de la localisation proche fournies en complément , comparer les écarts. Qu'en concluez vous ?

# De quelle la capitale européenne avez vous eu les données 
