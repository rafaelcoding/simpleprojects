while True:
    number = int(input('Type a number:'))
    he = hex(number) [2:]
    print(f'Hexadecimal:{he}')
    oc = oct(number) [2:]
    print(f'Octal:{oc}')
    bi = bin(number)[2:]
    print(f'Binary:{bi}')
