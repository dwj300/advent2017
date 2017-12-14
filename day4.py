#!/usr/bin/env python3

def unique(l):
    words = l.split()
    s = set(words)
    if len(words) == len(s):
        return True
    else:
        return False

def unique2(l):
    words = l.split()
    s_words = map(sorted, words)
    ss_words = map(lambda x: ''.join(x), s_words)
    return len(set(ss_words)) == len(words)

def runner(func):
    count = 0
    with open('4_in.txt') as f:
        for l in f.readlines():
            if func(l):
                count += 1
    return count

if __name__ == '__main__':
    assert(unique("aa bb cc dd ee"))
    assert(unique("aa bb cc dd aa") == False)
    assert(unique("aa bb cc dd aaa"))
    assert(unique2("abcde fghij"))
    assert(unique2("abcde xyz ecdab") == False)
    assert(unique2("a ab abc abd abf abj"))
    assert(unique2("iiii oiii ooii oooi oooo"))
    assert(unique2("oiii ioii iioi iiio") == False)
    print("Part 1: {0}".format(runner(unique)))
    print("Part 2: {0}".format(runner(unique2)))
