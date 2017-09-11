
# 5  | 5 | int
# 5.0  | 5.0 | float
# 5 % 2  | 1 | int
# 5 > 1  | True | boolean
# '5'  | '5' | string
# 5 * 2  | 10 | int
# '5' * 2  | 55 | string
# '5' + '2'  | '52' | string
# 5 / 2  | 2.5 | float
# 5 // 2  | 2 | int
# [5, 2, 1]  | [5, 2, 1] | int list
# 5 in [1, 4, 6]  | True | boolean

#Practice Exercise 1_2 (strings)

#a

a = "Supercalifragilisticexpialidocious"
print(len(a))

#b

print("\n")

a = "upercalifragilisticexpialidocious"
b = a.count('ice')
print(b)

#c

print("\n")

a = 'Antidisestablishmentarianism'
b = 'Honorificabilitudinitatibus'
lenght_a = len(a)
lenght_b = len(b)

if lenght_a > lenght_b:
    print('a is bigger than b')

else:
    print("a is not bigger than b")

#d

print("\n")

list_a = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
list_a.sort()
for i in list_a:
    print(i)

print ('Bartok het eerst en Buxtehude het laatst.')

#Practice Exercise 1_3

#1

int_a = 6
int_b = 7

#2

print("\n")

print((int_a + int_b) / 2)

#3

inventaris = ['papier', 'nietjes', 'pennen']

#4

voornaam = "Robin "
tussenvoegsel = "de"
achternaam = " Feijter"

#5

print("\n")

# waarom tussen haakjes?
mijnnaam = (voornaam + tussenvoegsel + achternaam)
print(mijnnaam)

#Practice Exercise 1_4

#1

print("\n")

print(6.75 > int_a)
print(6.75 < int_b)

#2

print("\n")

len_a = (len(inventaris))
len_b = (len(mijnnaam))

comp_len = (len_a / len_b)
print(comp_len > 5)

#3

print("\n")

lenght_inv = (len(inventaris))

result = (lenght_inv == 10 or lenght_inv == 0)
print(result)

#Practice Exercise 1_5

#1
#2
#3

print("\n")

list_1 = ['John', 'Alex']
list_1[-1] = 'Fredrick'
print(list_1)

#Practice Exercise 1_6

print("\n")

list_sum = [-1, 211, 3, 23, -12, 6, 7, 80]
var_a = min(list_sum)
var_b = max(list_sum)

print(var_b - var_a)

