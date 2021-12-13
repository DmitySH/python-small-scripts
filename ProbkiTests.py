import random

print('Enter name:')
name = input()
f = open('{}.txt'.format(name), 'w')
print('Enter n:')
n = int(input())
commands = ('+ ', '* ', '-', '-')
f.write(str(n) + '\n')
elems_in = 0
for i in range(n):
    if elems_in <= 0:
        ind = random.randint(0, 1)
    else:
        ind = random.randint(0, 3)
    f.write(commands[ind])
    if ind == 0 or ind == 1:
        f.write(str(i))
        elems_in += 1
    else:
        elems_in -= 1
    f.write('\n')
f.close()
