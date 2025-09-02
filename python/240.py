class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0 # start from the bottom-left corner

        while col < n and row >= 0: # stop when it reaches the top-right corner
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row - 1 # move up a row
            else:
                col = col + 1

        return False


def main():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

    sol = Solution().searchMatrix(matrix, 20)
    print(sol)


if __name__ == "__main__":
    main()