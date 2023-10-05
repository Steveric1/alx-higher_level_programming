#!/usr/bin/python3

for alpha in range(26):
    if alpha % 2 == 0:
        print('{:c}'.format(122 - alpha), end='')
    else:
        print('{:c}'.format(90 - alpha), end='')
