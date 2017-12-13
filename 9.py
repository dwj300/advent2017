#!/usr/bin/env python3

def score(stream):
    total = 0
    depth = 0
    garbage = False
    bang = False
    for s in stream:
        if not garbage:
            if s == '{':
                depth += 1
            elif s == '}':
                total += depth
                depth -= 1
            elif s == '<':
                garbage = True
        else:
            if bang:
                bang = False
            elif s == '!':
                bang = True
            elif s == '>':
                garbage = False
    return total

def score2(stream):
    total = 0
    garbage = False
    bang = False
    for s in stream:
        if not garbage:
            if s == '<':
                garbage = True
        else:
            if bang:
                bang = False
            elif s == '!':
                bang = True
            elif s == '>':
                garbage = False
            else:
                total += 1
    return total

if __name__ == "__main__":
    assert(score("{}") == 1)
    assert(score("{{{}}}") == 6)
    assert(score("{{},{}}") == 5)
    assert(score("{{{},{},{{}}}}") == 16)
    assert(score("{<a>,<a>,<a>,<a>}") == 1)
    assert(score("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9)
    assert(score("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9)
    assert(score("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3) 
    assert(score2("<>") == 0)
    assert(score2("<random characters>") == 17)
    assert(score2("<<<<>") == 3)
    assert(score2("<{!>}>") == 2)
    assert(score2("<!!!>>") == 0)
    assert(score2('<{o"i!a,<{i<a>') == 10)

    with open("9_in.txt") as f:
        stream = f.read().strip()
        print("Part 1: {0}".format(score(stream)))
        print("Part 2: {0}".format(score2(stream)))
