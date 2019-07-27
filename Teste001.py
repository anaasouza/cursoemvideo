nome = input('Qual o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))

nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:^10}!'.format(nome))
# ^ dentro das {} é para centralizar o resultado


n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print('A soma é {}, o produto é {} e a divisão é {}' .format(s, m, d))
print('Divisão inteira é {} e potência é {}' .format(di, p))

# na divisão quando o floot tiver muitas casas decimais posso restringir
#   print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d))
# No exemplo restringi em 3 casa decimais
# Se eu quiser tudo que estiver nos 'prints' na mesma linha e s´´ acrescentar no final da primeira
#  ,end=' '       # entre os dois últimos parenteses
#  para quebrar linha é só colocar  \n

# MÓDULOS
# >>> comando  >>> import e from                          (math= matemática)
# ceil - arredonda o número pra cima
# fllor - arredonda pra baixo
# pow - potência  = **
# sqrt - calcular a raiz quadrada
# factorial - cálcular o fatorial
# trunc - tranca o número... elimina tudo na frente da vírgula   sem arrendondar

# ex: >>>

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))

OU

from import math sqrt # ou especificar aqui o que vc quer da biblioteca
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))

>>>>>
import random
num = random.random() # número de 0 a 1
print(num)

#OU

import random
num = random.randint(1, 100)
print(num)

# Usar emoji

import emoji
print(emoji.emojize('Olá Mundo! :earth_americas:', use_aliases=True))