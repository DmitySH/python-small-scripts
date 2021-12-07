def make_dict(path='files/java_out.txt'):
    d = dict()
    with open(path, 'r') as file:
        for line in file:
            if 'got' in line:
                line = line.split()
                d[line[0]] = d.get(line[0], {'score': 0, 'from cards': 0,
                                             'stole': 0})

                d[line[0]]['score'] += int(line[2])
                d[line[0]]['from cards'] += int(line[2])

            elif 'from' in line:
                line = line.split()
                d[line[4]] = d.get(line[4], {'score': 0, 'from cards': 0,
                                             'stole': 0})
                d[line[4]]['score'] -= int(line[2])
                d[line[4]]['stole'] -= int(line[2])

                d[line[0]] = d.get(line[0],
                                   {'score': 0, 'from cards': 0,
                                    'stole': 0})

                d[line[0]]['score'] += int(line[2])
                d[line[0]]['stole'] += int(line[2])

            if 'has' in line:
                print(line, end='')
    sorted_d = sorted(d.items(), key=lambda x: x[0][-1])

    return sorted_d


if __name__ == '__main__':
    print('\n'.join(map(lambda x: str(x).replace("'", '')[1:-1], make_dict())))
