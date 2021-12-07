import random

n = random.randint(2, 10)

s = set()
m1 = -1
m2 = -1
while n > 0:
    new = random.randint(1, 10)
    if new not in s:
        print(new, end=' ')
        s.add(new)
        n -= 1
        if new > m1:
            m2 = m1
            m1 = new
        elif new > m2:
            m2 = new

print(0, ' max2 = ', m2)
