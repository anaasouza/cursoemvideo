# Faça um programa que leia um número inteiro e mostre seu sucesso e seu antecessor.

n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('O número é {}, o o antecessor é {} e seu sucessor é {}' .format(n, a, s))

# OU

n = int(input('Digite um número:'))
print('O número é {}, o o antecessor é {} e seu sucessor é {}' .format(n, (n-1), (n+1)))

# Crie um algoritimo que leia um número e mostre seu dobro, seu triplo, e sua raiz quadrada.

n = int(input('Digite um número:'))
print('O número é {}, o seu dobro é {}, seu triplo {} e sua raiz quadrada é {}' .format(n, (n*2), (n*3), (n**2)))

# Desenvolva um programa que leia duas notas de um aluno e calcule sua média.

n1 = int(input('Primeira nota:'))
n2 = int(input('Segunda nota:'))
print(' A média é {}' .format((n1+n2)/2))

# Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros.

m = float(input('Qual o tamanho?'))
print('O tamanho em metros é {}, \n em centimetros {} e \n em milimetros é {}' .format(m, (m*100), (m*1000)))

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n= int(input('Digite um numero:'))
a= (n*1)
b= (n*2)
c= (n*3)
d= (n*4)
e= (n*5)
f= (n*6)
g= (n*7)
h= (n*8)
i= (n*9)
j= (n*10)
print('Tabuada \n{}.1= {}' .format(n, a))
print('{}x2= {}' .format(n, b))
print('{}x3= {}' .format(n, c))
print('{}x4= {}' .format(n, d))
print('{}x5= {}' .format(n, e))
print('{}x6= {}' .format(n, f))
print('{}x7= {}' .format(n, g))
print('{}x8= {}' .format(n, h))
print('{}x9= {}' .format(n, i))
print('{}x10= {}' .format(n, j))

# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar. OBS. U$$ 1 = 3,27R$

cart = float(input('Quantos você tem na carteira?'))
print('Você pode comprar: {:.2f}U$$' .format(cart/3.27))

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessaria para pinta la sabendo que cada litro de tinta pinta uma área de 2m2.

l = float(input('Qual a largura da parede?'))
a = float(input('Qual a altura da parede?'))
area = (a*l)
tinta = (area/2)
print('A parede tem {} m² de área e precisa de {}l de tinta para pinta la.' .format(area, tinta))

# Faça um algoritimo que leia o preço de um produto e depois mostre o preço com 5% de desconto.

prod = float(input('Qual o preço do produto?'))
pd =(prod*0.95)
print('O valor do produto é {} e ele com 5% de desconto fica {}.' .format(prod, pd))

# Faça um algoritimo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento.

sl = float(input('Qual o seu salário atual?'))
sa = (sl*1.15)
print('O seu salário atual é R$ {} e com reajuste de 15% vai ficar R$ {}.' .format(sl, sa))

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
# Ex: Digite um número: 6.127. O número 6.127 tem a porção inteira 6.

import math
num = float(input('Digite um número:'))
pint = math.floor(num)
print('O número é {} e sua porção inteira é {}.' .format(num, pint))

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
hip = ()



# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome e mostre a ordem sorteada.

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.