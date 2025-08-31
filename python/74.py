class Solution:
    def round_half_up(self, x):
        if (x % 1 < 0.5):
            return int(x)
        return int(x) + 1

    def check_two_element_array(self, target: int, array: list[list[int]]) -> (int, bool):
        if len(array) != 2:
            raise ValueError("Length of this array must be 2")

        if array[0] == target:
            return (0, True)
        elif array[1] == target:
            return (1, True)
        else:
            return (1, False) # 1 is just a placeholder value

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Binary search on the columns first, and then the rows

        # Get no. of columns 
        no_of_rows = len(matrix)
        no_of_columns = len(matrix[0])
        print(f"Number of rows: {no_of_rows}")
    
        # Binary search 1: Time complexity of O(log(n))

        rows_to_be_searched = matrix
        print(f"rows to be searched are {rows_to_be_searched}")

        current_search = no_of_rows
        current_row = rows_to_be_searched[0]

        # Halve the structure
        # Check if target is less or more than the first element 
        # If more, check if it's more than the final element 
        # Reduce the matrix to only one row

        while len(rows_to_be_searched) > 1:
            current_search = self.round_half_up(len(rows_to_be_searched) / 2)
            print(f"searching {rows_to_be_searched}")
            print(f"current search: {current_search}")

            current_search_index = current_search - 1
            current_row = rows_to_be_searched[current_search_index]
            
            last_element = current_row[no_of_columns - 1]
            first_element = current_row[0]

            print(f"current row: {current_row}")

            if len(current_row) > 1:
                if target == first_element or target == last_element:
                    return True

                if target > first_element:
                    if target > last_element:
                        rows_to_be_searched = rows_to_be_searched[current_search:]    
                    elif target < last_element:
                        print(f"found in {current_row}")
                        break # row containing target discovered 
                else:
                    rows_to_be_searched = rows_to_be_searched[:current_search]
            else: # If the current row has only one element
                if target == current_row[0]:
                    return True
                else:
                    print(f"removing index {current_search_index} from {rows_to_be_searched}")
                    rows_to_be_searched.pop(current_search_index)

            current_row = rows_to_be_searched[0]
    
        print(f"search me: {current_row}")

        # Binary search 2: Time complexity of O(log(m))

        current_search = no_of_columns

        while len(current_row) > 1:
            current_search = self.round_half_up(len(current_row) / 2)
            print(f"current search: {current_search}")

            current_search_index = current_search - 1
            current_val = current_row[current_search_index]

            print(f"current search index: {current_search_index}")
            print(f"current val: {current_val}")

            if len(current_row) == 2:
                res = self.check_two_element_array(target, current_row)
                if res[1]:
                    print(f"Index {res[0]} of {current_row} = target {target}")
                    return True
                else:
                    return False

            if target > current_val:
                current_row = current_row[current_search:]
            elif target < current_val:
                current_row = current_row[:current_search]
            else: 
                print(f"Index {current_search_index} of {current_row} = target {target}")
                return True

            print(f"search me: {current_row}")

        # This part will only run if current_row was initially only one element
        if current_row[0] == target:
            return True

        return False



def main():
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # matrix = [[1]]
    # matrix = [[1],[3]]
    # matrix = [[1,1],[2,2]]
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]


    search_result = Solution().searchMatrix(matrix, 11)

    print(f"Search concluded with {search_result}")


if __name__ == "__main__":
    main()