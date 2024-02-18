print("Ingresa a continuación el número (entero y decimal) que deseas convertir")
numDecimal = int(input("-> "))

def decimToBinary(numDecimal):
    if numDecimal <= 0:
        return 0
    binario = ""

    while numDecimal>0:
        residuo = int(numDecimal % 2)
        numDecimal = int(numDecimal/2)
        binario = str(residuo) + binario
    return binario
    
binario = decimToBinary(numDecimal)
print(f"El número {numDecimal} en binario es {binario}")


binary = input("Ingresa un número binario: ")
def binaryToDecim(binary):
    position = 0
    decimal = 0
    binary = binary[::-1]
    for digit in binary:
        multiplier = 2**position
        decimal += int(digit) * multiplier
        position += 1
    return decimal
decimal = binaryToDecim(binary)
print(decimal)


def hexadecimal_a_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

def decimal_a_hexadecimal(decimal):
    hexadecimal = hex(decimal)[2:]
    return hexadecimal.upper()

def main():
    opcion = input("Ingrese '1' para convertir de hexadecimal a decimal, o '2' para convertir de decimal a hexadecimal: ")

    if opcion == '1':
        hexadecimal = input("Ingrese un número en hexadecimal de 3 dígitos: ")
        decimal = hexadecimal_a_decimal(hexadecimal)
        print("El número en decimal es:", decimal)
    elif opcion == '2':
        decimal = int(input("Ingrese un número entre 0 y 4095 para convertir a hexadecimal: "))
        if 0 <= decimal <= 4095:
            hexadecimal = decimal_a_hexadecimal(decimal)
            print("El número en hexadecimal es:", hexadecimal)
        else:
            print("El número ingresado no está en el rango válido (0 - 4095).")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
