import random

if __name__ == '__main__':
    for i in range(2):
        if random.randint(1, 100) > 35:
            print(random.randint(1, 50))
        else:
            print(random.randint(1, 100))

    pirates_number = random.randint(1, 300)
    print(pirates_number)
    while pirates_number > 0:
        next_group = random.randint(1, pirates_number)
        print(next_group)
        pirates_number -= next_group
