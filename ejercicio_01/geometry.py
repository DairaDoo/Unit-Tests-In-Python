def calcular_area_rectangulo(base, altura):
    """"
    Calcula el área de un rectángulo
    """

    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Base y altura deben ser números")

    if base < 0 or altura < 0:
        raise ValueError("Base y altura no pueden ser negativos")

    return base * altura