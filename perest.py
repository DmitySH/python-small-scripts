import itertools

a = [6, 4, 1, 5, 7, 2, 3]
b = [1, 2, 3, 4, 5, 6, 7]
perms = list(itertools.permutations(b, 7))
print(*perms)

for x in perms:
    # print(x[1])
    for i in range(0, 8):
        if x[a[i - 1] - 1] != a[x[i - 1] - 1]:
            break
    else:
        print(x)
