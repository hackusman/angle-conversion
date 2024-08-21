# Conversion entre Degrés et Radians

Ce script Python permet de convertir des angles entre degrés et radians. Il propose deux fonctionnalités principales :

1. **Conversion de degrés en radians**
2. **Conversion de radians en degrés**

## Prérequis

Assurez-vous que vous avez Python installé sur votre machine. Ce script utilise le module `math`, qui est inclus par défaut dans Python.

## Fonctionnalités

- **Conversion de degrés en radians** : Vous entrez un angle en degrés, et le script calcule et affiche la valeur équivalente en radians.
- **Conversion de radians en degrés** : Vous entrez un angle en radians, et le script calcule et affiche la valeur équivalente en degrés.

## Utilisation

1. **Exécutez le script Python** :
   ```bash
   python conversion_angles.py
   ```

2. **Entrez les valeurs demandées** :
   - Lorsque vous êtes invité à entrer un angle en degrés, saisissez la valeur souhaitée. Le script convertira cet angle en radians et affichera le résultat.
   - Ensuite, entrez un angle en radians lorsque vous y serez invité. Le script convertira cet angle en degrés et affichera le résultat.

## Exemple d'exécution

```bash
Valeur de l'angle en degrés : 45
La valeur en radians de l'angle entré est : 0.7854

Valeur de l'angle en radians : 1
La valeur en degrés de l'angle entré est : 57.2958
```

## Code Source

Voici le code source du script :

```python
import math

# Fonction pour convertir des degrés en radians
def degre_vers_radian(angle_degre):
    return angle_degre * math.pi / 180

# Fonction pour convertir des radians en degrés
def radian_vers_degre(angle_radian):
    return angle_radian * 180 / math.pi

# Lecture de la valeur de l'angle en degrés
angle_en_degre = float(input("Valeur de l'angle en degrés : "))

# Conversion de l'angle de degrés en radians
angle_en_radian = degre_vers_radian(angle_en_degre)
print(f"La valeur en radians de l'angle entré est : {angle_en_radian:.4f}")

# Lecture de la valeur de l'angle en radians
angle_en_radian_input = float(input("Valeur de l'angle en radians : "))

# Conversion de l'angle de radians en degrés
angle_en_degre_converti = radian_vers_degre(angle_en_radian_input)
print(f"La valeur en degrés de l'angle entré est : {angle_en_degre_converti:.4f}")
```
