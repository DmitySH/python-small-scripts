import matplotlib.pyplot as plt


def score_gen():
    for i in range(11):
        for j in range(11):
            if j != 0 and i != 0:
                yield i, j


axises = []
for x in score_gen():
    axises.append(((x[0] + x[1]) / 2, 2 * x[0] * x[1] / (x[0] + x[1]), x))
axises.sort()

plt.figure(1, figsize=(100, 20))
plt.yticks(range(11))
plt.plot([str(x[2]) for x in axises], [x[0] for x in axises], [x[1] for x in axises])

plt.figure(2, figsize=(100, 20))
plt.yticks(range(11))
plt.plot([str(x[2]) for x in axises], [round(x[0]) for x in axises], [round(x[1]) for x in axises])
plt.show()
