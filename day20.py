#!/usr/bin/env python3
import re
regex = 'p=<(\s?-?[0-9]+),(\s?-?[0-9]+),(\s?-?[0-9]+)>, v=<(\s?-?[0-9]+),(\s?-?[0-9]+),(\s?-?[0-9]+)>, a=<(\s?-?[0-9]+),(\s?-?[0-9]+),(\s?-?[0-9]+)>'
accel = lambda x: abs(x[6]) + abs(x[7]) + abs(x[8])
velo = lambda x: abs(x[3]) + abs(x[4]) + abs(x[5])
pos = lambda x: abs(x[0]) + abs(x[1]) + abs(x[2])
 
def part1(in_txt):
    distance = lambda p: abs(p[0]) + abs(p[1]) + abs(p[2])
    particles = [list(map(int, re.search(regex, l).groups())) for l in in_txt.split('\n')]
    orig = particles[:]
    min_a = min(particles, key=accel)
    particles = list(filter(lambda x: accel(x) == accel(min_a), particles))
    min_v = min(particles, key=velo)
    particles = list(filter(lambda x: velo(x) == velo(min_v), particles))
    min_p = min(particles, key=pos)
    particles = list(filter(lambda x: pos(x) == pos(min_p), particles))
    return orig.index(particles[0])

def part2(in_txt):
    particles = [list(map(int, re.search(regex, l).groups())) for l in in_txt.split('\n')]
    print(len(particles))
    temp = particles[:]
    for i in range(1000):
        temp = particles[:]
        for i in range(len(particles)):
            match = False
            pi = particles[i]
            for j in range(len(particles)):
                pj = particles[j]
                if i != j:
                    if pi[:3] == pj[:3] and pj in temp:
                        match = True
                        temp.remove(pj)
            if match and pi in temp:
                temp.remove(pi)
        particles = temp
        for p in particles:
            p[3] += p[6]
            p[4] += p[7]
            p[5] += p[8]
            p[0] += p[3]
            p[1] += p[4]
            p[2] += p[5]
    return len(particles)

if __name__ == "__main__":
    sample = "p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>\np=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"
    sample2 = "p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>\np=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>\np=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>\np=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"
    p1 = part1(sample)
    print(p1)
    assert(p1 == 0)
    p2 = part2(sample2)
    print(p2)
    assert(p2 == 1)
    with open("20_in.txt") as f:
        in_txt = f.read().strip()
        print("Part 1: {0}".format(part1(in_txt)))
        print("Part 2: {0}".format(part2(in_txt)))
