def minsizesubarray(nums,target):
    if sum(nums)<target:
        return -1
    left = 0
    windowsum = 0
    minlen = float("inf")

    for right in range(len(nums)):
        windowsum+=nums[right]
        while windowsum>=target:
            minlen = min(minlen,right-left+1)
            windowsum-=nums[left]
            left+=1
    return minlen

if __name__ == "__main__":
    print(minsizesubarray([2,3,1,2,4,3],7))