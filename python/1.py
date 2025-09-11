class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}

        # loop through nums
        # target - num. check if it's in dict. if not, add num to dict & move to next iteration

        # O(n) time complexity
        # O(n) space complexity
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_index:
                return (num_to_index[diff], i)
                break
            else:
                num_to_index[num] = i
                

            

def main():
    nums = [9,9,9,2,7,11,15]
    target = 9

    print(Solution().twoSum(nums, target))


if __name__ == "__main__":
    main()

