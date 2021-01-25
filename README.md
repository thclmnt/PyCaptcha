# PYCAPTCHA

PYCAPTCHA est un module python qui permet de créer simplement des Captcha pour vérifier qu'un utilisateur n'est pas un robot à l'aide de la bibliotèque Pillow.

## Installation

Effectuez la commande suivante pour installer le module de traitement d'image nécéssaire:

```bash
pip install pillow
```

Puis récupérez le fichier PYCAPTCHA.py et inserez le dans le dossier courant de votre projet.

## Utilisation

```python
import PYCAPTCHA as PC

#Création d'un test Captcha de type "math"
captcha = PC.Captcha("math")

#On sauvegarde l'image généré 
captcha.save("test.png")

#On affiche le résultat qu'on est censé obtenir
print(captcha.result)

```

## License
[MIT](LICENSE)
