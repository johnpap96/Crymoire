#!/usr/bin/env python
from __future__ import division
import random
import string

def swap_list_positions(_list, position, target):
    _list[position], _list[target] = _list[target], _list[position]
    return _list

def get_max_key(stats):
    """
    returns the key which yields the biggest value in a dictionary
    """
    inverse = [(value, key) for key, value in stats.items()]
    return max(inverse)[1]

def generate_random_key(size=1024, chars=string.printable):
    """
    returns a random key created from a selection of characters
    """
    return ''.join(random.choice(chars) for _ in range(size))

def charmod100(char):
    """returns ord of char mod 100"""
    return ord(char) % 100

def f_div(arith, paran):
    """
    returns a float division
    """
    return arith/paran