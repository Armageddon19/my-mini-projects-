# Card checker by Armageddon

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def validate_credit_card(card_number):
    # Verificar que el numero de tarjeta sea una cadena de dígitos
    if not card_number.isdigit():
        return False

    # Verificar la longitud común de los números de tarjetas de crédito (generalmente 13 a 19 dígitos)
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    return luhn_check(card_number)

# Ejemplo de uso:
card_number = input("Ingresa el numero de tarjeta de credito o debito: ") #This is my first language but the meaning is "enter the debit or credit card number" 
if validate_credit_card(card_number):
    print("El numero de la tarjeta es valido.") #The credit or debit card number is valid"
else:
    print("El numero de tarjeta es falso.")  #The credit or debit card number is fake"

