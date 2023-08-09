# método sort ordena a lista
x = [4, 1, 2, 3]
x.sort()
print(x)

# função sorted retorna uma lista de valores
y = sorted(x)
print(y)

"""
Para ordenar os elementos do maior para o menor, é possível especificar o 
parâmetro reverse = true.
Ao invés de comparar os próprios elementos da lista, é possível comparar 
os resultados de uma função que podemos especificar a partir do parametro key.
"""
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print(x)

# Outra maneira para ordenar listas de tuplas:
word_counts = [('suppose', 1), ('rose', 3), ('course', 2), ]
wc = sorted(word_counts,
            key=lambda wcs: wcs[1],
            reverse=True
            )
print(wc)

# list comprehensions
n = [x for x in range(0, 102) if x % 2 == 0]
print(n)

squares = [x * x for x in range(0, 10, 2)]
print(squares)

n_squares = [x * x for x in n]
print(n_squares)

# transformar listas em dicinarios ou conjuntos
square_dict = {x: x * x for x in range(0, 6)}
print(square_dict)

square_set = {x * x for x in [1, -2]}
print(square_set)

# se não precisarmos dos valores da lista, pode-se usar underscore _ como a var
# no caso abaixo estou criando um lista de mesmo tamanho de n, preenchida por 2
numbers_2 = [2 for _ in n]
print(numbers_2)

# formação de uma lista com multiplos for
pares_impares = [(x, y)
                 for x in range(0, 11, 2)
                 for y in range(1, 12, 2)
                 ]
print(pares_impares)

# apenas pares em que x < y
increasing_pairs = [(x, y)
                    for x in range(4)
                    for y in range(x + 1, 5)
                    ]
print(increasing_pairs)

"""
Um gerador (ou generator) é algo que você pode iterar sobre ( geralmente usando for), mas cujos valores são produzidos apenas conforme necessário(preguiçosamente).
O yield retém o estado da função onde ela é pausada (ao retornar o value).

Da próxima vez, quando um chamador chamar a função geradora - no nosso caso, o for - o corpo da função executará a instrução de onde ela foi pausada, em vez de executar a primeira instrução.
Uma maneira de criar geradores é com funções e o operador de yield:
"""
print("======================================")
x = 0


def lazy_range():
    """a lazy version of range"""
    for i in range(1, 4):
        yield i


valor = lazy_range()

print(list(valor))  # ele le e joga fora, logo no for i in valor não mostrará nada

print(valor)

for i in valor:
    print(i)

"""
continuação da aula01-Python Avançado

O loop seguinte vai consumir os valores lançados (yield) pela função lazy_range
um de cada vez até que não haja mais elementos para serem lançados:
"""

def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def do_something_with(value):
    print("Number:", value)


for i in lazy_range(10):
    do_something_with(i)

"""
Criando uma sequência infinita de números com geradores
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

for i in natural_numbers():
    print(i)

"""
"""
O Python 3 já oferece alguns iteradores preguiçosos para produzir loops eficientes. O iterador count(start, step) produz números a partir de um valor inicial start e com um passo step definido como parâmetro (o valor padrão do passo é 1):

from random import random
from itertools import count

print('count(10) com parada aleatória:')
for i in count(10):
    if random() < 0.8:
        print(i, end=" ")
    else:
        break

print('\ncount(1,2) com parada aleatória:')        
for i in count(1, 2):
    if random() < 0.8:
        print(i, end=" ")
    else:
        break   

Outros iteradores preguiçosos interessantes são o cycle e o `repeat:
from itertools import repeat, cycle
print("cycle('ABCD') com parada aleatória:")
for letter in cycle('ABCD'):
    if random() < 0.95:
        print(letter, end=" ")
    else:
        break

print("\nrepeat(10,3):")
for i in repeat(10,3):
    print(i, end=" ")

Você pode usar a função islice para fazer com que os iteradores acima gerem sequências finitas.

from itertools import count, islice

print("Interrompe a geração de count(10) quando 2 números forem gerados:")
for number in islice(count(10), 2):
    print(number, end=" ")

print("\nInterrompe a geração count(1,3) quando 10 números forem gerados:")
for number in islice(count(1, 3), 10):
    print(number, end=" ")

O outro lado de construir geradores preguiçosos é que você só pode iterar através deles uma única vez. Se precisar de iterar através deles várias vezes, você precisará recriar o gerador a cada vez ou usar uma lista.

"""

# Aleatoriedade

import random

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

"""
A função random.random() produz números uniformemente distribuídos entre 0 e 1.
O módulo random, na verdade, produz números pseudo-aleatórios, ou seja, eles dependem de um estado interno (ou semente) que você pode alterar usando random.seed. Isso serve para podermos reproduzir (ou repetir) os resultados gerados a partir de códigos que processam sequências de números aleatórios.
"""
random.seed(10) #atribui 1 à semente
print('Primeio número: ', random.random())
random.seed(10) #atribui 1 à semente novamente
print('Primeio número: ', random.random())

"""
Iremos usar random.randrange as vezes. Essa função recebe 1 ou 2 argumentos e retorna um elemento escolhido aleatoriamente entre o range() correspondente:
a = random.randrange(10) # range(10) = 0, 1, ..., 9
b = random.randrange(30, 60) # range(3, 6) = 30, 31, ..., 60
print(a,b)

Existem outros poucos métodos que nós acharemos conveniente usar, como o random.shuffle, que rearranja os elementos de uma lista de forma aleatória:

up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

Se você precisa de um elemento aleatório de uma lista você pode usar random.choice
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print(my_best_friend)

Se você precisar escolher uma amostra aleatória de elementos sem reposição, você pode usar random.sample:

lottery_numbers = list(range(60))
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

Para escolher uma amostra de 
 elementos com reposição você pode fazer uma chamada para random.choices passando 
 como parâmetro:

four_with_replacement = random.choices(list(range(3)), k=4)
print(four_with_replacement)
"""