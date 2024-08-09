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


def decomposition_monnaie(nombre_a_decomposer: float) -> str:
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
    def decompisition_recursive(nombre: float, indice: int = 0) -> str:
        """Décompose le nombre par une méthode récursive"""

        if nombre == 0 or indice >= len(DEVISE_MEXICAINE):
            return ""

        montant = list(DEVISE_MEXICAINE)[indice]
        designation = DEVISE_MEXICAINE[montant]
        nb_devise = int(nombre // montant)
        reste = round(nombre % montant, 2)

        decomposition = f"{designation}: {nb_devise}{'\n'}" if nb_devise else ""

        return f"{decomposition}{decompisition_recursive(reste, indice + 1)}"

    if not isinstance(nombre_a_decomposer, int | float) or (type(nombre_a_decomposer) is float and len(str(nombre_a_decomposer).split(".")[1]) > 2):
        raise ValueError("l'argument doit être un nombre avec au maximum 2 chiffres après la virgule.")

    return decompisition_recursive(nombre_a_decomposer)[:-1]


if __name__ == '__main__':
    print(decomposition_monnaie(8432.20))
    # import doctest
    # if doctest.testmod().failed == 0:
    #     print("C'est tout bon!")
