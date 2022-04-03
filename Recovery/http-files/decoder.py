#!/usr/bin/env python3

import sys

KEY = b'MVxsXCVbUaJWjsl' # Replace with key from /opt/.fixutil/backup.txt
FILE_PATH = sys.argv[1]

def generate_long_key(key: bytes, target_length: int) -> bytes:
    while len(key) < target_length:
        key += key
    return key

with (open(FILE_PATH, 'rb')) as f:
    c = f.read()
    k = generate_long_key(KEY, len(c))
    p = bytes(a ^ b for a, b in zip(c, k)).decode()

with (open(FILE_PATH, 'w')) as f:
    f.write(p)

KEY = b'AdsipPewFlfkmll' # Replace with key from /opt/.fixutil/backup.txt
FILE_PATH = sys.argv[1]

def generate_long_key(key: bytes, target_length: int) -> bytes:
    while len(key) < target_length:
        key += key
    return key

with (open(FILE_PATH, 'rb')) as f:
    c = f.read()
    k = generate_long_key(KEY, len(c))
    p = bytes(a ^ b for a, b in zip(c, k)).decode()

with (open(FILE_PATH, 'w')) as f:
    f.write(p)
