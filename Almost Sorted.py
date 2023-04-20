def checkAlmostSorted(nums):
    # test whether nums[lo:hi+1] is sorted or not
    def isSorted(nums, lo, hi):
        i = lo + 1
        while i <= hi:
            if nums[i] < nums[i - 1]:
                return False
            i += 1
        return True

    def exch(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    if isSorted(nums, 0, len(nums) - 1):
        print("yes")
    else:
        sortedNums = nums[:]
        sortedNums.sort()

        # find the leftmost index which nums[idx] != sortedNums[idx]
        lIdx = 0
        while lIdx < len(nums) and nums[lIdx] == sortedNums[lIdx]:
            lIdx += 1

        # find the rightmost index
        rIdx = len(nums) - 1
        while rIdx >= 0 and nums[rIdx] == sortedNums[rIdx]:
            rIdx -= 1
        # nums is not sorted, so there are at least 2 indexes out of place.

        # test if we can just swap to get sorted nums
        exch(lIdx, rIdx)
        if isSorted(nums, lIdx, rIdx):
            print("yes")
            print("swap %d %d" % (lIdx + 1, rIdx + 1))
        else:
            # test if we can reverse the segments to get a sorted array
            exch(lIdx, rIdx) # swap back
            seg = nums[lIdx:rIdx+1]
            seg.reverse()
            if isSorted(seg, 0, len(seg)- 1):
                print("yes")
                print("reverse %d %d" % (lIdx + 1, rIdx + 1))
            else:
                print("no")

if __name__ == "__main__":
    n = input()
    nums = list(map(int, input().split(" ")))
    checkAlmostSorted(nums)
