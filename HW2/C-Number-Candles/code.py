"""
References: Prof Yan Gu's slides: 05-Greedy -> Homework Deadlines and Buying Gifts example 

By using Greedy Algorithm:

The plan is to have a maximum number of candle digits by buying as much as the cheapest candles as possible
For each digit position (from left to right), replace it with the largest digit that still allows enough money to fill the remaining positions with the cheapest digit.

Time Complexity: O(N), where N: max number of digits <- M // min_price
                 and loop 1 is independent from the nested for loop hence O(N)
"""
monies = int(input().strip())
prices = list(map(int, input().split()))


min_price = min(prices)
length = monies // min_price # max candles that can be bought when used on min price

result = []
rem_money = monies


for pos in range(length):
    # start from max cost to have as first like on the left side then to lower to find max possible to be bought
    for d in range(9, 0, -1):
        cost_d = prices[d - 1]

        rem_pos = length - pos - 1
        if rem_money - cost_d >= rem_pos * min_price:
            result.append(str(d))
            rem_money -= cost_d
            break   


print(''.join(result))