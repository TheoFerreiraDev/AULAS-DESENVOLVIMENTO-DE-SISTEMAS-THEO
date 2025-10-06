def classificar_idade(idade):
        if idade < 12 and idade >= 1 :
            return "Criança"
        if idade >= 12 and idade <= 17 :
            return "Adolescente"
        if idade >= 17 and idade < 230 :
            return "Adulto"
        else:
            return "idade Invalida"



def maiorNumero(numero1, numero2):
    if numero1 > numero2:
        return 'O primeiro número é maior que o segundo número'
    elif numero2 > numero1:
        return 'O segundo número é maior que o primeiro número'
    else:
        return 'Os dois são iguais'


def vogalConsoante(letra):
    letra = str(input("Digite uma letra: "))
    if letra == 'a' and 'e' and 'i' and 'o' and 'u':
        return"A letra que você digitou é uma vogal"
    else:
        return "A letra que você digitou é uma consoante"


def senhaIgual(senha1,senha2):
    senha1 = str(input('Digite a sua senha: '))
    senha2 = str(input('Repita a sua senha: '))
    if senha1 == senha2:
        print('Acesso permitido')
    else:
        print('Acesso negado')

def passado(nota1,nota2,nota3,media,media_final)
    nota1 = float(input('Digite a primeira nota: '))
    nota2= float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = nota1 + nota2 + nota3
    media_final = media / 3
    if media_final >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

def reverse(numero1,numero2,numero3,numeros):
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    numero3 = int(input('Digite o terceiro número: '))
    numeros = [numero1, numero2, numero3]
    numeros.reverse()
    return numeros

def consumo(tempo,velocidade,litros_usados):
    tempo = float(input('Quantas tempo levou a viagem: '))
    velocidade = float(input('Qual foi a velocidade média: '))
    distancia = tempo * velocidade
    litros_usados = distancia /12
    return f'A quantidade de litros usados foi de: {litros_usados}L'
