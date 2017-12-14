#!/usr/bin/env python3
import sys
steps = {"ne": (1,0,-1), "se": (1,-1,0), "s": (0,-1,1), "sw": (-1,0,1), 
         "nw": (-1,1,0), "n": (0,1,-1)}

def distance(moves):
    (x,y,z) = (0,0,0)
    for m in moves:
        (x,y,z) = map(sum, zip((x,y,z), steps[m]))
    return (abs(x) + abs(y) + abs(z)) / 2

def part2(moves):
    (x,y,z) = (0,0,0)
    locations = []
    for m in moves:
        (x,y,z) = map(sum, zip((x,y,z), steps[m]))
        locations.append((x,y,z))
    return max(map(lambda a: ((abs(a[0])+abs(a[1])+abs(a[2]))/2), locations))
        
if __name__ == "__main__":
    assert(distance("se,sw,se,sw,sw".split(',')) == 3)
    assert(distance("ne,ne,s,s".split(','))  == 2)
    assert(distance("ne,ne,ne".split(',')) == 3)
    assert(distance("ne,ne,sw,sw".split(',')) == 0)

    with open('11_in.txt') as f:
        moves = f.read().strip().split(',')
        print("Part 1: {0}".format(distance(moves)))
        print("Part 2: {0}".format(part2(moves)))
