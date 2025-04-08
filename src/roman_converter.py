def decimal_to_roman(decimal):
    """
    Convierte un número decimal a número romano.
    
    Args:
        decimal: Número entero entre 1 y 3999
    
    Returns:
        str: Representación en números romanos
    """
    if not isinstance(decimal, int):
        raise TypeError("El número debe ser un entero")
    if not 1 <= decimal <= 3999:
        raise ValueError("El número debe estar entre 1 y 3999")

    conversion_table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    roman = ""
    for value, symbol in conversion_table:
        while decimal >= value:
            roman += symbol
            decimal -= value
    
    return roman
