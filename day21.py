#!/usr/bin/env python3
import numpy as np
from math import sqrt
def part1(it, in_txt):
    size = 3
    pattern = np.array(list(map(list, ".#./..#/###".split('/'))))
    #rules = [(np.array(list(map(list, l.split('=')[0].strip().split('/')))), np.array(list(map(list, l.split('>')[1].strip().split('/'))))) for l in in_txt.split('\n')]
    rules = {''.join(l.split('=')[0].strip().split('/')): np.array(list(map(list, l.split('>')[1].strip().split('/')))) for l in in_txt.split('\n')} 
    for i in range(it):
        m = 3
        if size % 2 == 0:
            m = 2 
        newarray = np.array(0)
        for x in range(0, size, m):
            newrow = np.array(0)
            for y in range(0, size, m):
                square = pattern[x:x+m, y:y+m]
                options = [square, np.fliplr(square), np.flipud(square), np.transpose(square), np.flipud(np.fliplr(square)),
                           np.transpose(np.flipud(square)), np.transpose(np.fliplr(square)),
                           np.transpose(np.flipud(np.fliplr(square)))]
                options_str = list(map(lambda x: "".join(x.ravel()), options))

                for (o, n) in rules.items():
                    if o in options_str:
                        if newrow.size == 1:
                            newrow = n
                        else:
                            newrow = np.append(newrow, n, axis=0)
                        break
            if newarray.size == 1:
                newarray = newrow
            else:
                newarray = np.append(newarray, newrow, axis=1)
        pattern = newarray
        size = len(pattern)
    return list(np.ravel(pattern)).count('#')

if __name__ == "__main__":
    sample = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"
    #p1 = part1(2, sample)
    #print(p1)
    #assert(p1 == 12)
    with open("21_in.txt") as f:
        in_txt = f.read().strip()
        #print("Part 1: {0}".format(part1(5, in_txt)))
        print("Part 2: {0}".format(part1(18, in_txt)))
