import time
import random
print('Bem-Vindo ao jogo! Sua terefa será acertar um número que irei gerar e dar dicas para que você acerte o número gerado.')
time.sleep(6)
print('Preparado(a)?')
time.sleep(1)
print('Ok!. Vou deixar você escolher um intervalo de números, desse intervalo irei gerar o número.')
time.sleep(2)
n1 = int(input('Insira o Primeiro número do intervalo: '))
while n1 < 0:
    n1 = int(input('Por favor, digite o primeiro número, apartir de 0: '))
n2 = int(input('Digite o último número do intervalo: '))
while n2 < 0:
    n2 = int(input('Por favor, digite o último número, apartir de 0: '))
gerado = random.randrange(n1, n2+1, 1)
print('Gerando um número para você...')
time.sleep(3)
acertou = False
adivinhe = int(input('Chute um número: '))
while acertou == False:
    if adivinhe == gerado:
        acertou = True
    elif adivinhe < gerado:
        adivinhe=int(input('Digite um número maior: '))
    elif adivinhe > gerado:
        adivinhe=int(input('Digite um número menor: '))
print('PARABÉNS, VOCÊ ACERTOU!!! O NÚMERO É {}'.format(gerado))