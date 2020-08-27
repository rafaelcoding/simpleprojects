while True:
    número = int(input('Digite um número:'))
    he = hex(número) [2:]
    print(f'Hexadecimal:{he}')
    oc = oct(número) [2:]
    print(f'Octal:{oc}')
    bi = bin(número)[2:]
    print(f'Binário:{bi}')
