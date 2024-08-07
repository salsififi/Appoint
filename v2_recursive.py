"""
Même chose que dans main.py, mais en utilisant la récursivité
"""

DEVISE_MEXICAINE: dict[int, str] = {
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


def decomposition_monnaie(nombre: float, indice: int = 0) -> str:
    """
    Décompose le nombre passé en argument de façon à donner le nombre de pièces
    et billets pour le constituer (n'affiche pas les pièces et billets dont on n'a pas besoin).
    >>> print(decomposition_monnaie(145.80))
    billete 100 pesos: 1
    billete 20 pesos: 2
    moneda 5 pesos: 1
    moneda 50 centavos: 1
    moneda 20 centavos: 1
    moneda 10 centavos: 1
    >>> print(decomposition_monnaie(74))
    billete 50 pesos: 1
    billete 20 pesos: 1
    moneda 2 pesos: 2
    >>> print(decomposition_monnaie(1001.20))
    billete 1000 pesos: 1
    moneda 1 peso: 1
    moneda 20 centavos: 1
    >>> decomposition_monnaie(123.45678)
    Traceback (most recent call last):
    ...
    ValueError: l'argument doit être un nombre avec au maximum 2 chiffres après la virgule.
    >>> decomposition_monnaie("tagada")
    Traceback (most recent call last):
    ...
    ValueError: l'argument doit être un nombre avec au maximum 2 chiffres après la virgule.
    """
    if not isinstance(nombre, int | float) or (type(nombre) is float and len(str(nombre).split(".")[1]) > 2):
        raise ValueError("l'argument doit être un nombre avec au maximum 2 chiffres après la virgule.")

    if nombre == 0 or indice >= len(DEVISE_MEXICAINE):
        return ""

    montant = list(DEVISE_MEXICAINE)[indice]
    designation = DEVISE_MEXICAINE[montant]
    nb_devise = int(nombre // montant)
    reste = round(nombre % montant, 2)

    decomposition = f"{designation}: {nb_devise}{'\n' if decomposition_monnaie(reste, indice + 1) else ''}" \
        if nb_devise else ""

    return f"{decomposition}{decomposition_monnaie(reste, indice + 1)}"


if __name__ == '__main__':
    print(decomposition_monnaie(8432.20))
    # import doctest
    # if doctest.testmod().failed == 0:
    #     print("C'est tout bon!")

# DEVISE_MEXICAINE = {
#     1000: "billete 1000 pesos",
#     500: "billete 500 pesos",
#     200: "billete 200 pesos",
#     100: "billete 100 pesos",
#     50: "billete 50 pesos",
#     20: "billete 20 pesos",
#     10: "moneda 10 pesos",
#     5: "moneda 5 pesos",
#     2: "moneda 2 pesos",
#     1: "moneda 1 peso",
#     0.5: "moneda 50 centavos",
#     0.2: "moneda 20 centavos",
#     0.1: "moneda 10 centavos",
# }
#
#
# def decomposition_monnaie_recursive(nombre: float, index: int = 0) -> str:
#     # Base de la récursion
#     if nombre <= 0 or index >= len(DEVISE_MEXICAINE):
#         return ""
#
#     montant = list(DEVISE_MEXICAINE.keys())[index]
#     designation = DEVISE_MEXICAINE[montant]
#
#     # Calculer le nombre de billets/pièces de ce montant
#     count = int(nombre // montant)
#     remainder = nombre % montant
#
#     # Si on a au moins une de ces billets/pièces, les ajouter au résultat
#     if count > 0:
#         return f"{designation}: {count}\n{decomposition_monnaie_recursive(remainder, index)}"
#     else:
#         return decomposition_monnaie_recursive(nombre, index + 1)
#
#
# # Exemple d'utilisation
# nombre = 1234.5
# resultat = decomposition_monnaie_recursive(nombre)
# print(resultat)
