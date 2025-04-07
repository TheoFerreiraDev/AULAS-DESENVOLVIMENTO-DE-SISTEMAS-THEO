idade = int (input('Informe sua idade: '))
if idade < 12:
    print('Criança')
    print(idade)
elif idade >=12 and idade <=17:
    print('Adolecente')
    print(idade)
else:
    print('Adulto')
    print(idade)

EXERCÍCIO 02
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print('O primeiro número é maior que o segundo número')
elif numero2 > numero1:
    print('O segundo número é maior que o primeiro número')
else:
    print('Os dois são iguais')

EXERCÍCIO 03
letra = str(input("Digite uma letra: "))
if letra == 'a' and 'e' and 'i' and 'o' and 'u':
    print("A letra que você digitou é uma vogal")
else:
    print("A letra que você digitou é uma consoante")


EXERCÍCIO 04
senha1 = str(input('Digite a sua senha: '))
senha2 = str(input('Repita a sua senha: '))
if senha1 == senha2:
    print('Acesso permitido')
else:
    print('Acesso negado')


EXERCÍCIO 05
nota1 = float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = nota1 + nota2 + nota3
media_final = media / 3
if media_final >= 7:
    print('Aprovado')
else:
    print('Reprovado')

EXERCÍCIO 06
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numeros = [numero1, numero2, numero3]
numeros.reverse()
print(numeros)


EXERCÍCIO 07
tempo = float(input('Quantas tempo levou a viagem: '))
velocidade = float(input('Qual foi a velocidade média: '))
distancia = tempo * velocidade
litros_usados = distancia /12
print (f'A quantidade de litros usados foi de: {litros_usados}L')
