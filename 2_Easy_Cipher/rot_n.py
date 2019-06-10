# $ python rot_n.py s rot
import sys

def _rot_n(c, n):
    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + int(n)) % 26 + ord('a'))

    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + int(n)) % 26 + ord('A'))

    return c

def _rot(s, n):
    c = (_rot_n(c, n) for c in s)
    print( ''.join(c))

if __name__ == '__main__':
    param = sys.argv
    s = param[1]
    rot = param[2]
    _rot(s, rot)