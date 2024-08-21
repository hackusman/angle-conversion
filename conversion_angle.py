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
