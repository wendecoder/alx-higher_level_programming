#!/usr/bin/python3
def infinite_add(nums):
    inputs = len(nums) - 1
    if inputs == 0:
        print("{:d}".format(inputs))
    else:
        j = 1
        sum = 0
        while j <= inputs:
            sum += int(nums[j])
            j += 1
        print("{:d}".format(sum))
if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
