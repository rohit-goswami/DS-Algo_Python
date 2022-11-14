# Best Time to Buy and Sell Stock
---

`amazon` `apple` `adobe` 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit* you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output:5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```
**Constraints:**
* ``` 1 <= prices.length <= 105```
* ```0 <= prices[i] <= 104```

**Solutions:**

### Approach 1: Brute force : Time complexity O($n^2$) 

```python=
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit , profit = 0, 0
        for index, value in enumerate(prices):
            for j in prices[index+1:]:
                if j > value:
                    profit = j - value
                    if(profit > max_profit): max_profit = profit

        return max_profit
        
```

### Approach 2: Divide and Conquer : Time complexity O($n$) 

```python=
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit , min_buy_price = 0, prices[0]
        for price in prices:
            max_profit_temp = price - min_buy_price
            max_profit = max(max_profit_temp, max_profit)
            min_buy_price = min(price, min_buy_price)
        return max_profit
        
```
