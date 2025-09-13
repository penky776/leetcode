class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        triplets = set() # O(n) space
        already_processed = set() # numbers that we've already found all the combinations for. O(n) space
 
        nums.sort() # O(nlog(n)) tc

        # [-1, -1, 1, 2, 4, 5, 6, 8]
        for i, val in enumerate(nums): 
            if val in already_processed:
                continue

            two_sum = -val # val + two_sum = 0 . we need to get all possible couples that equate to two_sum
            start = i + 1

            for n2 in range(start, len(nums)):
                diff = two_sum - nums[n2]
                # binary search on remaining portion to find diff. Note: index of diff should NOT be n2

                h, l = len(nums) - 1, n2 + 1

                while l <= h:
                    mid = (h + l) // 2

                    if nums[mid] == diff:
                        triplets.add((val, nums[n2], nums[mid]))
                        break
                    elif nums[mid] < diff:
                        l = mid + 1
                    elif nums[mid] > diff:
                        h = mid - 1

            already_processed.add(val)

        return [list(t) for t in triplets]



def main():
    nums = [-1,0,1,2,-1,-4]

    sol = Solution().threeSum(nums)
    print(sol)
    # overall: O(n^2) space. O(n^2log(n)) time

if __name__ == "__main__":
    main()