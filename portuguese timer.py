from time import sleep


segundos = int(input('Digite quantos segundos você quer que eu espere: '))
print('Vou começar em')

sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('Esperando...')

for cont in range(segundos, -1, -1):
    print(cont)
    sleep(1)
print('Acabou')
