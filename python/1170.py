class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        lex_counts_for_words = [] # O(n) space complexity

        for word in words:
            lex_count = 0
            lex_char = None
            for char in word:
                if lex_char is None or char < lex_char:
                    lex_char = char
                    lex_count = 1
                elif char == lex_char:
                    lex_count += 1
                
            lex_counts_for_words.append(lex_count)

        lex_counts_for_words.sort() # O(nlog(n)) time complexity

        answer = []

        for query in queries: 
            lex_count = 0
            lex_char = None
            for char in query:
                if lex_char is None or char < lex_char:
                    lex_char = char
                    lex_count = 1
                elif char == lex_char:
                    lex_count += 1
            
            # binary search against lex_counts_for_words for each query's lex_count
            high, low = len(lex_counts_for_words), 0
            
            while low < high:
                mid = (high + low) // 2 # new length

                if lex_counts_for_words[mid] <= lex_count:
                    # shift right
                    low = mid + 1 
                else:
                    high = mid # move left
                
            answer.append(len(lex_counts_for_words) - low)

        return answer


def main():
    pass

if __name__ == "__main__":
    main()