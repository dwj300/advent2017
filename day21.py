#!/usr/bin/env python3
import numpy as np

def part1(it, in_txt):
    size = 3
    pattern = np.array(list(map(list, ".#./..#/###".split('/'))))
    rules = [(np.array(list(map(list, l.split('=')[0].strip().split('/')))), np.array(list(map(list, l.split('>')[1].strip().split('/'))))) for l in in_txt.split('\n')]
    for i in range(it):
        print("pattern:")
        print(pattern)
        m = 3
        if size % 2 == 0:
           m = 2 
        newarray = np.array(0)
        print("size {0}, m {1} len {2}".format(size, m, len(pattern)))
        for x in range(0, size, m):
            newrow = np.array(0)
            for y in range(0, size, m):
                square = pattern[x:x+m, y:y+m]
                options = [square, np.fliplr(square), np.flipud(square), np.transpose(square), np.flipud(np.fliplr(square)), np.transpose(np.flipud(square)), np.transpose(np.fliplr(square)), np.transpose(np.flipud(np.fliplr(square)))]
                for (o, n) in rules:
                    if len(o) != len(square):
                        continue
                    

                    #print(options)
                    try:
                        foo = list(map(lambda c: len(c) == len(o) and all(np.ravel(c) == np.ravel(o)), options))
                    except:
                        pass
                        #import pdb; pdb.set_trace()
                    #print(foo)
                    if any(foo):
                        #square = n
                        #print(n)
                        #print(newrow)
                        old = newrow.size
                        if newrow.size == 1:
                            newrow = n
                        else:
                            newrow = np.append(newrow, n, axis=0)
                        print("old: {0} new: {1}".format(old, newrow.size))
                        break
            if newarray.size == 1:
                newarray = newrow
                print("here")
            else:
                newarray = np.append(newarray, newrow, axis=1)
        pattern = newarray
        size = len(pattern)
    print(pattern)
    return list(np.ravel(pattern)).count('#')

def part2(in_txt):
    return 0

if __name__ == "__main__":
    sample = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"
    p1 = part1(2, sample)
    print(p1)
    assert(p1 == 12)
    assert(part2(sample) == 0)
    with open("21_in.txt") as f:
        in_txt = f.read().strip()
        print("Part 1: {0}".format(part1(5, in_txt)))
        print("Part 2: {0}".format(part2(in_txt)))
