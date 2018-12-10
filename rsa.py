from gmpy2 import mpz, is_prime, powmod

print('achando p')
p = mpz('110082100')
while True:
    print(p)
    if is_prime(p):
        if p % 6 == 5:
            break
    p = p + 1
print('achando q')
q = mpz('278234000')
while True:
    print(q)
    if is_prime(q):
        if q % 6 == 5:
            break
    q = q + 1
print('p =', p, 'q =', q)
n = p*q
print('n =', n)

l = mpz('3')
print('l =', 3)
blocos=(11,22,33,44,55,66,77,88,99)
print('blocos =', blocos)
cod=[]

for i in range(len(blocos)):
    cod.append(powmod(blocos[i], l, n))
    print(cod)

d = mpz((((q-1)*(p-1)-4)*4/6)+3)
print('d =', d)

decod=[]
for i in range(len(blocos)):
    decod.append(powmod(cod[i], d, n))
    print(decod)

print('fim')
