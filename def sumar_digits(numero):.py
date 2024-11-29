def sumar_digits(numero):
    """Suma els dígits del número i retorna la suma."""
    suma = 0
    for digit in str(numero):
        suma += int(digit)
    return suma

def main():
    # Demanar un número a l'usuari
    numero = int(input("Introdueix un número: "))

    # Sumar els dígits
    suma_digits = sumar_digits(numero)

    # Mostrar la suma
    print(f"La suma dels dígits de {numero} és: {suma_digits}")

    # Comprovar si la suma és parell o senar
    if suma_digits % 2 == 0:
        print("La suma és parell.")
    else:
        print("La suma és senar.")

# Executar el programa
if __name__ == "__main__":
    main()