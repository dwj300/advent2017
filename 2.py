#!/usr/local/bin/python3
def calc(lines):
    s = 0
    for l in lines:
        nums = l.split()
        nums = list(map(int, nums))
        s += max(nums) - min(nums)
    return s

def calc2(lines):
    s = 0
    for l in lines:
        nums = list(map(int, l.split()))
        for i, n in enumerate(nums):
            for n2 in nums[i+1:]:
                if n % n2 == 0:
                    s += n // n2
                elif n2 % n == 0:
                    s += n2 // n
    return s

if __name__ == '__main__':
    assert(calc(["5 1 9 5", "7 5 3", "2 4 6 8"]) == 18)
    assert(calc2(["5 9 2 8", "9 4 7 3", "3 8 6 5"]) == 9)
    with open("2_in.txt") as f:
        print("Part 1: {0}".format(calc(f.readlines())))
        f.seek(0)
        print("Part 2: {0}".format(calc2(f.readlines())))

