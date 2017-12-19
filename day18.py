#!/usr/bin/env python3
import string

def part1(in_txt):
    instructions = in_txt.split('\n')
    registers = {k:0 for k in list(string.ascii_lowercase)}
    last_sound = 0
    i = 0
    while i < len(instructions) and i >= 0:
        instruction = instructions[i]
        parts = instruction.split(' ')

        if parts[0] == "set":
            try:
                registers[parts[1]] = int(parts[2])
            except:
                registers[parts[1]] = registers[parts[2]]
        elif parts[0] == "add":
            registers[parts[1]] += int(parts[2])
        elif parts[0] == "snd":
            last_sound = registers[parts[1]]
        elif parts[0] == "mul":
            try:
                registers[parts[1]] *= registers[parts[2]]
            except:
                registers[parts[1]] *= int(parts[2])
        elif parts[0] == "mod":
            try:
                registers[parts[1]] %= int(parts[2])
            except:
                registers[parts[1]] %= registers[parts[2]]
        elif parts[0] == "rcv" and registers[parts[1]] != 0:
            return last_sound
        elif parts[0] == "jgz" and registers[parts[1]] > 0:
            i += int(parts[2]) - 1
        i += 1

def other(i):
    if i == 1:
        return 0
    else:
        return 1

def part2(in_txt):
    instructions = in_txt.split('\n')
    registers = [{k:0 for k in list(string.ascii_lowercase)}, {k:0 for k in list(string.ascii_lowercase)}]
    registers[1]['p'] = 1
    send = [[],[]]
    pc = [0,0]
    cur = 0
    count = 0
    alive = [True, True]
    while (alive[0] or alive[1]) and ((pc[0] < len(instructions) and pc[0] >= 0) or (pc[1] < len(instructions) and pc[1] >= 0)):
        instruction = instructions[pc[cur]]
        parts = instruction.split(' ')
        #print("Curent {0}, parts: {1}".format(cur, parts))
        if parts[0] == "set":
            try:
                registers[cur][parts[1]] = int(parts[2])
            except:
                registers[cur][parts[1]] = registers[cur][parts[2]]
        elif parts[0] == "add":
            try:
                registers[cur][parts[1]] += int(parts[2])
            except:
                registers[cur][parts[1]] += registers[cur][parts[2]]
        elif parts[0] == "snd":
            try:
                send[other(cur)].append(int(parts[1]))
            except:
                send[other(cur)].append(registers[cur][parts[1]])
            print("[{0}]-{1}sending{2}".format(pc[cur], cur, send[other(cur)]))
            if cur == 1:
                count += 1
                cur = 0
            else:
                cur = 1
            pc[other(cur)] += 1
            pc[cur] -= 1
        elif parts[0] == "mul":
            try:
                registers[cur][parts[1]] *= registers[cur][parts[2]]
            except:
                registers[cur][parts[1]] *= int(parts[2])
        elif parts[0] == "mod":
            try:
                registers[cur][parts[1]] %= int(parts[2])
            except:
                registers[cur][parts[1]] %= registers[cur][parts[2]]
        elif parts[0] == "rcv":
            if len(send[cur]) > 0:
                print("{0}Receiving{1}".format(cur,send[cur][0]))
                registers[cur][parts[1]] = send[cur].pop(0)
                alive[cur] = True
            else:
                if cur == 0 and not alive[1]:
                    return count
                elif cur == 1 and not alive[0]:
                    return count
                else:
                    alive[cur] = False
                    if cur == 0:
                        cur = 1
                    else:
                        cur = 0
                    pc[cur] -= 1
        elif parts[0] == "jgz":
            cond = None
            try:
                cond = registers[cur][parts[1]] 
            except:
                cond = int(parts[1])
            if cond > 0:
                try:
                    pc[cur] += int(parts[2]) - 1
                except:
                    pc[cur] += registers[cur][parts[2]] - 1
        pc[cur] += 1
        
        if pc[cur] >= len(instructions) or pc[cur] < 0:
            alive[cur] = False
            if cur == 1:
                cur = 0
            else:
                cur = 1
    return count


if __name__ == "__main__":
    sample = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
    sample2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
    assert(part1(sample) == 4)
    assert(part2(sample2) == 3)
    with open("18_in.txt") as f:
        in_txt = f.read().strip()
        print(in_txt)
        print("Part 1: {0}".format(part1(in_txt)))
        print("Part 2: {0}".format(part2(in_txt)))
