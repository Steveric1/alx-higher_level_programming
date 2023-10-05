#!/usr/bin/python3

for alpha in range(ord('z'), ord('a') - 1, -1):
    if alpha % 2 == 0:
        print('{:s}'.format(chr(alpha)).upper(), end='')
    else:
        print('{:s}'.format(chr(alpha)), end='')
