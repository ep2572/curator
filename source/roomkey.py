"""
---------------------
Random Roomkey Generator
---------------------
"""

import random

alnum = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
keychain = {"": 1}


def get_roomkey():
    random.seed()
    seq = ""
    while seq in keychain:
        seq = ""
        for n in range(0, 12):  # Current size of sequence: 12
            seq += alnum[random.randrange(0, 61)]
    keychain[seq] = 1
    return seq
