from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

s = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])

ret = 0
fail = 0
with open("in") as f:
    
    for x in f.read().splitlines():
        if x == '':
            print(s)
            if len(s) == 0 and not fail:
                ret += 1
            fail = 0
            s = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
        else:
            for t in x.split(' '):
                q = t.split(':')
                o, v = q
                if o in s:
                    if o == 'byr':
                        try:
                            if int(v) < 1920 or int(v) > 2002:
                                raise
                        except:
                            fail = 1
                    elif o == 'iyr':
                        try:
                            if int(v) < 2010 or int(v) > 2020:
                                raise
                        except:
                            fail = 1
                    elif o == 'eyr':
                        try:
                            if int(v) < 2020 or int(v) > 2030:
                                raise
                        except:
                            fail = 1
                    elif o == 'hgt':
                        p, pp = v[-2:], v[:-2]
                        if p == 'cm':
                            try:
                                if int(pp) < 150 or int(pp) > 193:
                                    raise
                            except:
                                fail = 1
                        elif p == 'in':
                            try:
                                if int(pp) < 59 or int(pp) > 76:
                                    raise
                            except:
                                fail = 1
                        else:
                            fail = 1
                    elif o == 'hcl':
                        try:
                            if len(v) != 7:
                                raise
                            if v[0] != '#':
                                raise
                            for i in range(1, 7):
                                if not ('0' <= v[i] <= '9') and not ('a' <= v[i] <= 'f'):
                                    raise
                        except:
                            fail = 1
                    elif o == 'ecl':
                        try:
                            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                raise
                        except:
                            fail = 1
                    elif o == 'pid':
                        try:
                            if len(v) != 9:
                                raise
                            for c in v:
                                if not '0' <= c <= '9':
                                    raise 
                        except:
                            fail = 1
                    s.discard(o)
                    print(o, v, fail)
    if len(s) == 0 and not fail:
        ret += 1
    print(ret)