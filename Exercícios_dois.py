#1)Peça ao usuário para digitar 5 números e mostre a soma deles ao final:
#Exercício 1:
valorA = int(input("Digite um valor: "))
valorB = int(input("Digite um segundo valor: "))
valorC = int(input("Digite um terceiro valor: "))
valorD = int(input("Digite um quarto valor: "))
valorE = int(input("Digite um quarto valor: "))


soma = (valorA + valorB + valorC + valorD + valorE)
print(soma)

#2)Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor:
#Exercício 2:
valorA = int(input("Digite um valor: "))
valorB = int(input("Digite um segundo valor: "))
valorC = int(input("Digite um terceiro valor: "))
valorD = int(input("Digite um quarto valor: "))


lista = [valorA, valorB, valorC, valorD]
print(min(lista))
print(max(lista))
 
#3)Peça ao usuário uma palavra e mostre quantas vogais ela tem:
#Exercício 3:
contador = 0
palavra = input("Digite uma palavra: ")
lista_vogais = ['a', 'e', 'i', 'o', 'u']


for letra in palavra:
    for vogal in lista_vogais:
        if(letra == vogal):
            contador += 1


print(f'O Número de vogais na palavra {palavra} é de {contador}')


#4)Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados:
#Exercício 4:
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int (input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int (input("Digite o quinto numero: "))
numero6 = int(input("Digite o sexto numero: "))


lista_pares = []
lista_numeros = [numero1, numero2, numero3, numero4, numero5, numero6]


for numero_digitado in lista_numeros:
    if numero_digitado % 2 == 0:
        lista_pares.append(numero_digitado)
if len(lista_pares) == 0:
    print(f'Lista de numeros {lista_numeros} não possui nenhum numero par' )


else:
    print(f'A lista digitada contém os seguntes números pares {lista_pares}')

#5)Solicite as notas de 4 provas e mostre a média:
#Exercício 5:
valorA = float(input("Digite sua primeira nota: "))
valorB = float(input("Digite sua segunda nota: "))
valorC = float(input("Digite sua terceira nota: "))
valorD = float(input("Digite sua quarta nota: "))


som_media = (valorA + valorB + valorC + valorD )
media_final = (som_media / 4)
print (media_final)

#6)Peça ao usuário um número e mostre a tabuada desse número de 1 a 10:
#Exercício 6:
numeroDigitado = int(input("Digite um número: "))
for numero in range(1,11):
    print(f"{numeroDigitado} x {numero} = {numeroDigitado * numero}")




#7)Peça um número N ao usuário e mostre todos os números de 1 até N:
#Exercício 07:
numeroDigitado = int(input("Digite um número: "))


for numero in range(1,numeroDigitado + 1):
  print(f'{numero}')

#8)Peça ao usuário uma palavra e mostre ela ao contrário:
#Exercício 08:
palavraDigitada= input("Digite uma Palavra: ")


palavraReversa =  palavraDigitada [:: -1]


print(f'O contrário da palavra {palavraDigitada} é: {palavraReversa}')

#9)Peça um número ao usuário e diga se ele é múltiplo de 3:
#Exercício 09:
numeroDigitado = int(input(“Digite um número: “))
if numeroDigitado %3== 0:
    print(f'o numero {numeroDigitado} é multiplo de 3')
else:
    print (f'O numero {numeroDigitado} não é multiplo de 3')

#10)Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética:
#Exercício 10:
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")


listaDeNomes = [nome1, nome2, nome3]


listaDeNomes.sort(reverse=False)


print(f'Os nomes em ordem alfabética são: {listaDeNomes}')

