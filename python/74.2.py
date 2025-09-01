class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        (m, n) = (len(matrix), len(matrix[0]))
        high = m*n - 1
        low = 0
        
        while low <= high:
            middle = (high + low) // 2

            row = middle // n
            column = middle % n

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                low = middle + 1
            elif matrix[row][column] > target:
                high = middle - 1

        return False




def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # matrix = [[1]]
    # matrix = [[1],[3]]
    # matrix = [[1,1],[2,2]]
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]


    search_result = Solution().searchMatrix(matrix, 3)

    print(f"Search concluded with {search_result}")


if __name__ == "__main__":
    main()