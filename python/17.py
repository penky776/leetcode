phone = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        import itertools

        len_digits = len(digits)
        if not (0 <= len_digits <= 4):
            raise Exception("Number of digits invalid")

        digits = list(map(int, digits))

        for digit in digits:
            if digit not in range(2, 10):
                raise ValueError("invalid digits")
        
        solution = []
        if not (len_digits == 0):
            self.recurse_me(solution, "", digits, 0)        

        return solution

    def recurse_me(self, solution: List[str], current: str, digits: List[int], current_index: int):
        if current_index == len(digits):
            solution.append(current)
            return

        for char in phone[digits[current_index]]:
            self.recurse_me(solution, current + char, digits, current_index + 1)