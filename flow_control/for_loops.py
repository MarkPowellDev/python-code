
import math

print(f'pi = {math.pi:.3f}.')

for y in range(1, 11):
    print('{} '.format(y))

print('---------- b  -------------')
for b in range(1, 11):
    print('b',b)

print('---------- a -------------')
count = 1
for a in range(1, 11):
    print(f'a', "_", count)
    count += 1

print('---------- x -------------')
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:6d}'.format(x, x*x, x*x*x))

print('---------- c -------------')
for c in range(0, 11):
    print('c', c)

print('---------- d -------------')
for d in range(5, 11):
    print('d', d)

print('---------- i -------------')
for i in range(5):
    print(i)

 #   message1 = 'Hello Again {} ({})'.format(name, age)

