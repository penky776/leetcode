class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A) < len(B): # B must be the shorter one
            A, B = nums2, nums1
        
        m, n = len(A), len(B)
        
        total = m + n
        half = total // 2

        # [4, 5, 6, 7, 8, 9] => A 6/2 = 3
        # [1, 2, 3] => B 3//2 = 1 
        # Total = [1, 2, 3, 4, 5, 6, 7, 8, 9] median = 5 index = 4 half = 9 // 2 = 4

        # binary search on B (shorter one)
        l, r = 0, n 

        while True:
            j = (l + r) // 2 # B partition boundary . 1
            i = half - j # A partition boundary . 3

            # inf to handle out of range 
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # check if partitioned correctly
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                l = j + 1   # move partition right in B
            else:
                r = j - 1   # move partition left in B


def main():
    # nums1 = [1]
    # nums2 = []
    # nums1 = [1,2]
    # nums2 = [3,4]
    nums1 = [1,2,3,4,5] # 2
    nums2 = [6,7,8,9,10,11,12,13,14,15,16,17,18] # 5    


    median = Solution().findMedianSortedArrays(nums1, nums2)

    print(median)


if __name__ == "__main__":
    main()