import random

n = random.randint(2, 20)
# 7 3 2 15 1 9 11 5 4 6 8 23 0
s = set()
m1 = -1
m2 = -1
while n > 0:
    new = random.randint(1, 45)
    if new not in s:
        print(new, end=' ')
        s.add(new)
        n -= 1
        if new > m1:
            m2 = m1
            m1 = new
        elif new > m2:
            m2 = new

print(0)
