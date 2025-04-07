#EXERCÍCIO 02
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))


if num1 > num2:
    print ("num1 é maior que num2")
elif num2 > num1:
    print("num2 é maior que num1")
else:
    print("os dois são iguais")


#EXERCÍCIO 03
letra = str(input("Digite uma letra: "))
if letra == 'a' and 'e' and 'i' and 'o' and 'u':
    print("Sua letra é uma vogal")
else:
    print("Sua letra é uma consoante")


#EXERCÍCIO 04
senha1 = str(input("Digite a sua senha: "))
senha2 = str(input("Repita a sua senha: "))


if senha1 == senha2:
    print("Acesso permitido")
else:
    print("Acesso negado")


#EXERCÍCIO 05
nota1 = float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = nota1 + nota2 + nota3
media_final = media / 3


if media_final >= 7:
    print("Aprovado")
else:
    print("Reprovado")



#EXERCÍCIO 06

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o primeiro numero: "))
numeros = [num1, num2, num3]
numeros.reverse()
print(numeros)


#EXERCÍCIO 07
tempo_viagem = float(input("Digite quantas horas teve a viagem: "))
velocidade = float(input("Digite a velocidade aproximada: "))
distancia = tempo_viagem * velocidade
litros = distancia/12
print(f"A quantidade de litros utilizada foi de: {litros}")
