class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0                                        # temp to store max profit
        new  = prices[0]                                # 2nd pointer to check new indexes

        for i in prices[1:]:                            # looping thru he array excluding the first elem
            if (i > new):                               # if current elem is bigger than previous
                temp = max(temp, (i-new))               # update temp pointer
            else:
                new = i                                 # update the new pointer
                
        return temp                                     # returns 0 if there were no profitable sales

# second attempt
        # temp = 0                                        # temp to store max profit
        # for i in range(len(prices)):                    # loop thru the array
        #     if ((max(prices[i:])) - prices[i]) > temp:  # check if a sale would make a bigger temp
        #         temp = max(prices[i:]) - prices[i]      # update temp 
        # return temp                                     # returns 0 if there were no profitable sales

# initial solution        
        # temp = 0                                  # temp to store max profit
        # for i in range(len(prices)):              # loop thru the array
        #     for j in range(i, i+len(prices[i:])): # second pointer to track profit
        #         if not (prices[i] > prices[j]):
        #             if ((prices[j] - prices[i]) > temp):
        #                 temp = (prices[j] - prices[i])
        # return temp # returns 0 if there were no profitable sales
