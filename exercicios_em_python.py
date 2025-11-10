# 1. Classificação de Idade
# Peça a idade do usuário e classifique-o de acordo com a tabela:
# Menor de 12 anos → Criança
# Entre 12 e 17 anos → Adolescente
# 18 anos ou mais → Adulto

def classificar_idade(idade):
    if idade < 12 and idade >= 1:
        return 'Criança'
    elif idade >= 12 and idade <= 17:
        return 'Adolescente'
    elif idade >= 18 and idade <= 100:
        return 'Adulto'
    else:
        return 'Idade Inválida' 

# 2. Maior de Dois Números
# Solicite dois números ao usuário e exiba o maior deles. Caso sejam iguais, informe isso.

def comparar_numeros(numero1, numero2):
    if numero1 > numero2:
        return f'{numero1} é maior que {numero2}'
    elif numero1 == numero2:
        return f'{numero1} é igual a {numero2}'
    else:
        return f'{numero1} é menor que {numero2}'

# 3. Verificação de Vogal ou Consoante
# Peça ao usuário para digitar uma letra e informe se é uma vogal (a, e, i, o, u) ou consoante.

def comparar_vogal_consoante(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return f'A letra digitada é uma vogal'
    else:
        return f'A letra digitada é uma consoante'
    
# 4. Comparação de Senhas
# Solicite ao usuário que defina uma senha e, em seguida, peça para confirmá-la. Caso as senhas sejam iguais, exiba “Acesso permitido”, senão, exiba “Senhas não coincidem”.

def comparar_senhas(senha, senhaconfirmada):
    if(senha == senhaconfirmada):
        return 'Acesso permitido!'
    else:
        return 'Acesso negado!'
    
# 5. Cálculo de Média e Aprovação
# Peça ao usuário para digitar três notas e calcule a média. Se a média for maior ou igual a 7, o aluno está aprovado, caso contrário, está reprovado.

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7 and media <= 10:
        return f'O aluno está aprovado com média: {media}!'
    elif media < 7 and media >= 0:
        return f'O aluno está reprovado com média: {media}!'
    else:
        return f'Média inválida!'
    
# 6. Escreva um programa que leia 3 números inteiros e imprima na tela os valores em ordem decrescente

def numeros_ordem_decrescente(numero1, numero2, numero3):
    listaDeNumeros = [numero1, numero2, numero3]

    return f'A lista dos números em ordem decrescente é: {sorted(listaDeNumeros,reverse=True)}'

# 7. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz
#   12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média.
#   Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
#   Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a
#   fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
#   tempo gasto, a distância percorrida e a quantidade de litros utilizada na viagem. Dica: trabalhe com valores reais.

def litros_usados_combustivel (tempogasto, velocidademedia):

    distancia = tempogasto * velocidademedia
    litrosUsados = distancia / 12

    return f'A quantidade de litros usados na viagem foi de: {litrosUsados}L'
import unittest

from exerciciosteste import *

class TestesExemplos(unittest.TestCase):

   def testar_classificar_idade(self):
      self.assertEqual(classificar_idade (10), 'Criança')
      self.assertEqual(classificar_idade (15), 'Adolescente')
      self.assertEqual(classificar_idade (34), 'Adulto')
      self.assertEqual(classificar_idade (150), 'Idade Inválida')

   def testar_comparador_numeros(self):
      self.assertEqual(comparar_numeros(10, 13), '10 é menor que 13')
      self.assertEqual(comparar_numeros(22, 17), '22 é maior que 17')
      self.assertEqual(comparar_numeros(33, 33), '33 é igual a 33')

   def testar_comparar_vogal_consoante(self):
      self.assertEqual(comparar_vogal_consoante('a'), 'A letra digitada é uma vogal')
      self.assertEqual(comparar_vogal_consoante('b'), 'A letra digitada é uma consoante')

   def testar_comparar_senhas(self):
      self.assertEqual(comparar_senhas(123, 123), 'Acesso permitido!')
      self.assertEqual(comparar_senhas('abc', 'def'), 'Acesso negado!')

   def testar_calcular_media(self):
      self.assertEqual(calcular_media(8, 8, 8), 'O aluno está aprovado com média: 8.0!')
      self.assertEqual(calcular_media(3, 3, 3), 'O aluno está reprovado com média: 3.0!')
      self.assertEqual(calcular_media(11, 11, 11), 'Média inválida!')

   def testar_numeros_ordem_decrescente(self):
      self.assertEqual(numeros_ordem_decrescente(5, 7, 6), 'A lista dos números em ordem decrescente é: [7, 6, 5]')
       
   def testar_litros_usados_combustivel(self):
      self.assertEqual(litros_usados_combustivel(1, 120), 'A quantidade de litros usados na viagem foi de: 10.0L')

if __name__ == "__main__":

    unittest.main()
