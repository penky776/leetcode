class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A) < len(B):
            A, B = nums2, nums1

        if len(A) == 0:
            A = B
        elif len(B) == 0:
            B = A
        
        m, n = len(A), len(B)
        half_A, half_B = m//2, n//2
        
        total = m + n
        if (total % 2 == 0):
            index_left_B = max(half_B - 1, 0)
            index_left_A = max(half_A - 1, 0)

            left_partition_end = max(B[index_left_B], A[index_left_A])
            right_parition_end = min(B[half_B ], A[half_A])
            avg = (left_partition_end + right_parition_end) / 2
            return avg
        else: # if it’s odd
            median = min(A[half_A], B[half_B])
            return median



def main():
    # nums1 = [1]
    # nums2 = []
    # nums1 = [1,2]
    # nums2 = [3,4]
    nums1 = [1,2,3,4,5] # 2
    nums2 = [6,7,8,9,10,11,12,13,14,15,16,17,18] # 5
    # output = 3, expected = 9
    median = Solution().findMedianSortedArrays(nums1, nums2)

    print(median)


if __name__ == "__main__":
    main()