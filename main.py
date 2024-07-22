"""
L'APPOINT
Challenge Discord n°16 du serveur Docstring
(https://discord.com/channels/396825382009044994/1160339200063844356/1262331902518624256)
Date: 2024-07-22
"""

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


def decomposition_monnaie(nombre: float) -> str:
    """
    Décompose le nombre passé en argument de façon à donner le nombre de pièces
    et bhillets pour le constituer (n'affiche pas les pièces et billets dont on n'a pas besoin).
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

    decomposition = []
    reste = nombre
    for montant, designation in DEVISE_MEXICAINE.items():
        if reste > montant:
            decomposition.append(f"{designation}: {int(reste // montant)}")
            reste = reste % montant
    return "\n".join(decomposition)


if __name__ == '__main__':
    print(decomposition_monnaie(1001.20))
    # import doctest
    # if doctest.testmod().failed == 0:
    #     print("C'est tout bon!")
