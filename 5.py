#!/usr/local/bin/python3

def exit(steps, incr):
    cur = 0
    count = 0
    while cur >= 0 and cur < len(steps):
        temp = cur
        cur = cur + steps[cur]
        steps[temp] += incr(steps[temp])
        count += 1
    return count

if __name__ == '__main__':
    part_1_func = lambda x: 1
    part_2_func = lambda x: -1 if x >= 3 else 1
    assert(exit([0, 3, 0, 1, -3], part_1_func) == 5)
    assert(exit([0, 3, 0, 1, -3], part_2_func) == 10)
    with open('5_in.txt') as f:
        print("Part 1: {0}".format(exit(list(map(int, f.read().split())), part_1_func)))
        f.seek(0)
        print("Part 2: {0}".format(exit(list(map(int, f.read().split())), part_2_func)))

