# Appoint
Un script pour rendre la monnaie en pesos mexicains 😊, en réponse à un challenge niveau débutant proposé sur le serveur Discord "Docstring":
(https://discord.com/channels/396825382009044994/1160339200063844356/1262331902518624256)

Consigne:

Caramba ! En voyage solo au Mexique, vous avez perdu votre carte de crédit 😥. Il ne vous reste plus que billets et pièces locales. Le comble dans tout ça, les commerçants ne rendent pas la monnaie !

👉  Le but de ce challenge est de développer une fonction decomposition_monnaie() qui affiche le nombre minimal de billets et de pièces nécessaires pour reconstituer n'importe quelle somme.

🔹 Étapes

    Déterminer pour chaque pièce et billet mexicain s'il doit faire partie de la somme et en quelle quantité.
    Construire une chaîne de caractères qui sera retournée par la fonction.


🔹 Conditions

    L'affichage se fait via la console.
    La somme à reconstituer est à envoyer en argument à la fonction : decomposition_monnaie(nombre).
    La fonction retourne une chaîne de caractères où à chaque ligne une valeur monétaire est associée au nombre de fois qu'elle est nécessaire. Les pièces et billets non utilisés dans la décomposition ne doivent pas apparaître.


🔹 Ressource
Les différents billets et pièces du peso :

DEVISE_MEXICAINE = {
    1000: "billete 1000 pesos",
    500: "billete 500 pesos",
    200: "billete 200 pesos",
    100: "billete 100 pesos",
    50: "billete 50 pesos",
    20: "billete 20 pesos",
    10: "moneda 10 pesos",
    5: "moneda 5 pesos",
    2: "moneda 2 pesos",
    1: "moneda 1 peso",
    0.5: "moneda 50 centavos",
    0.2: "moneda 20 centavos",
    0.1: "moneda 10 centavos",
}


🔹 Exemples

print(decomposition_monnaie(145.80))

billete 100 pesos: 1
billete 20 pesos: 2
moneda 5 pesos: 1
moneda 50 centavos: 1
moneda 20 centavos: 1
moneda 10 centavos: 1


print(decomposition_monnaie(74))

billete 50 pesos: 1
billete 20 pesos: 1
moneda 2 pesos: 2


print(decomposition_monnaie(1001.20))

billete 1000 pesos: 1
moneda 1 peso: 1
moneda 20 centavos: 1
