import os
import sys


def walker(catalog):
    lines = [0, 0]
    folders = os.listdir(catalog)
    for x in folders:
        next_path = os.path.join(catalog, x)
        if os.path.isfile(next_path):
            with open(next_path, 'r', encoding="latin") as f:
                comments = 0
                lines_sum = 0
                for line in f:
                    if line.strip().startswith('/') or line.strip() \
                            .startswith('*') \
                            or line.strip().startswith('#'):
                        comments += 1
                    lines_sum += 1
                lines[0] += lines_sum
                lines[1] += lines_sum - comments
                print(x, lines_sum, lines_sum - comments)
        else:
            next_folder_lines = walker(next_path)
            lines[0] += next_folder_lines[0]
            lines[1] += next_folder_lines[1]
    return lines


if __name__ == '__main__':
    catalog = input("Enter path to catalog ")
    print(walker(catalog))
