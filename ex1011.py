print("Ex01")

def primos_no_intervalo(a, b):
    primos = []
    for n in range(a, b + 1):
        if n <= 1:
            continue
        e_primo = True 
        for i in range(2, n):
            if n % i == 0:
                e_primo = False 
                break
        if e_primo:
            primos.append(n)
    return primos
print(f"Resultado: {primos_no_intervalo(10, 20)}") 
print(" ")
############################################################################################
############################################################################################
print("Ex02")
def ordenar_sem_repeticao(lista):
    lista_sem_repeticao = []
    for item in lista:
        if item not in lista_sem_repeticao:
            lista_sem_repeticao.append(item)
    lista_ordenada = sorted(lista_sem_repeticao)
    return lista_ordenada

lista_com_duplicatas = [5, 2, 8, 2, 5, 1, 8]
print(f"Lista Original: {lista_com_duplicatas}")
print(" ")
############################################################################################
############################################################################################
print("Ex03")

def soma_digitos(n):
    texto_numero = str(abs(n))
    soma_total = 0
    for digito_texto in texto_numero:
        digito_inteiro = int(digito_texto)
        soma_total = soma_total + digito_inteiro
    return soma_total

print(f"Soma dos dígitos de 456: {soma_digitos(456)}") 
print(" ")
############################################################################################
print("Ex04")

def eh_palindromo(texto):
    t_sem_espaco = texto.replace(" ", "")
    t_limpo = t_sem_espaco.lower()
    tamanho = len(t_limpo)
    for i in range(tamanho // 2):
        caractere_frente = t_limpo[i]
        caractere_tras = t_limpo[tamanho - 1 - i]
        if caractere_frente != caractere_tras:
            return False 
    return True
frase_palindromo = "A base do teto desaba"
print(f"'{frase_palindromo}' é palíndromo? {eh_palindromo(frase_palindromo)}") 
print(" ")
############################################################################################
print("Ex05")

def frequencia_palavras(texto):
    freq = {}
    palavras = texto.lower().split()
    for palavra in palavras:
        if palavra in freq:
            freq[palavra] = freq[palavra] + 1 
        else:
            freq[palavra] = 1
    return freq

texto_exemplo = "Eu amo programar, e você ama programar também"
print(f"Frequência: {frequencia_palavras(texto_exemplo)}")
print(" ")
############################################################################################
print("Ex06")

def media_lista(lista):
    if len(lista) == 0:
        return None  
    soma = sum(lista)
    quantidade = len(lista)
    return soma / quantidade

lista_numeros = [10, 20, 30, 40]
print(f"Média de {lista_numeros}: {media_lista(lista_numeros)}")
print(f"Média de lista vazia: {media_lista([])}")

print(" ")
