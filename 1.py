#!/usr/bin/env python3

def inverse_captcha(seq):
    s = 0
    for i in range(0, len(seq)):
        n = i + 1 if i != len(seq) - 1 else 0
        if seq[i] == seq[n]: s += seq[i]
    return s

def inverse_captcha_part2(seq):
    return sum(map(lambda i: seq[i], filter(lambda i: (seq[i] == seq[(i + len(seq) //2) % len(seq)]), range(0, len(seq)))))

if __name__ == '__main__':
    assert(inverse_captcha([1,1,2,2]) == 3)
    assert(inverse_captcha([1,1,1,1]) == 4)
    assert(inverse_captcha([1,2,3,4]) == 0)
    assert(inverse_captcha([9,1,2,1,2,1,2,9]) == 9)
    assert(inverse_captcha_part2([1,2,1,2]) == 6)
    assert(inverse_captcha_part2([1,2,2,1]) == 0)
    assert(inverse_captcha_part2([1,2,3,4,2,5]) == 4)
    assert(inverse_captcha_part2([1,2,3,1,2,3]) == 12)
    assert(inverse_captcha_part2([1,2,1,3,1,4,1,5]) == 4)
    with open('1_in.txt') as f:
        seq = [int(x) for x in f.read().strip()]
        print("Part 1: {0}".format(inverse_captcha(seq)))
        print("Part 2: {0}".format(inverse_captcha_part2(seq)))

