#!/usr/bin/python3
def infinite_add(nums):
    inputs = len(nums) - 1
    sum = 0
    for i in range(1, inputs + 1):
        sum += int(nums[i])

    print("{:d}".format(sum))
if __name__ == '__main__':
    import sys
    infinite_add(sys.argv)
