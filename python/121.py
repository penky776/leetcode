class Solution:
	def get_max_profit(self, prices: list[int]) -> int:

		# Brute force method
		# for loop
		# buying date, difference between the next elements and our current element.
		# brute force method => method 1 => time complexity of O(n^2) TOO LARGE
	
		
        l, r = 0, 1
        m_profit = 0 

        while r < len(prices):
            if prices[r] < prices[l]: #if no profit
                l = r
            else:
                new_profit = prices[r] - prices[l] #selling price - buying price
                m_profit = max(new_profit, m_profit)
            r += 1
    
        return m_profit

		



def main():
    prices = [7,1,5,3,6,4]

    Solution().maxProfit(prices)


if __name__ == "__main__":
    main()