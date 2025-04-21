def int_a_romano(num):
    valores_romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    resultado = ""

    for valor, simbolo in valores_romanos:
        while num >= valor:
            resultado += simbolo
            num -= valor

    return resultado

def main():
    print("Conversor de números decimales a romanos")
    try:
        numero = int(input("Ingresá un número entre 1 y 3999: "))
        if 1 <= numero <= 3999:
            romano = int_a_romano(numero)
            print(f"El número romano es: {romano}")
        else:
            print("El número debe estar entre 1 y 3999.")
    except ValueError:
        print("Por favor, ingresá un número válido.")

if __name__ == "__main__":
    main()