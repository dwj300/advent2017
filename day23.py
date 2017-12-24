#!/usr/bin/env python3
from math import sqrt
from string import ascii_letters

def value(registers, x): 
    try:
        return int(x)
    except:
        return registers[x]

def part1(in_txt):
    count = 0
    registers = {k:0 for k in ascii_letters[:8]}
    lines = in_txt.split('\n')
    pc = 0
    while pc >= 0 and pc < len(lines):
        instr, x, y = lines[pc].split(' ')
        if instr == "jnz" and value(registers, x) != 0:
            pc += value(registers,y) - 1
        elif instr == "set": registers[x] = value(registers,y)
        elif instr == "sub": registers[x] -= value(registers,y)
        elif instr == "mul":
            count += 1
            registers[x] *= value(registers,y)
        pc += 1
                    
    return count

def not_prime(n):
    if n % 2 == 0 and n > 2: 
        return True
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return True
    return False

def part2(): return sum(map(not_prime, range(106500, 123501, 17)))

if __name__ == "__main__":
    with open("23_in.txt") as f:
        in_txt = f.read().strip()
        p1 = part1(in_txt)
        print("Part 1: {0}".format(p1))
        assert(p1 == 3969)
        p2 = part2()
        print("Part 2: {0}".format(p2))
        assert(p2 == 917)
