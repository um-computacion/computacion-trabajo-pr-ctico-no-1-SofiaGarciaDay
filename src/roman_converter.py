def decimal_a_romano(numero):

    valores_romanos = [
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
    
    romano = ""
    
    for valor, simbolo in valores_romanos:
        while numero >= valor:
            romano += simbolo
            numero -= valor
            
    return romano

numero = int(input("Ingresa un número decimal entre 1 y 3999: "))

if 1 <= numero <= 3999:
    print(f"El número {numero} en romano es: {decimal_a_romano(numero)}")
else:
    print("El número ingresado no está en el rango válido (1-3999).")
