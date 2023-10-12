"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

sys.maxsize: system max size

To solve this question in a linear time, we have to consider two things:
1) Track max profit. It is tempting to init it as -sys.maxsize, but profit cannot be negative, so init with 0
2) Track minimum price of the stock to know the min value.

"""
import pdb
import sys

prices = [7,1,5,3,6,4]

def bestStockTrade_bf(prices):
    len_list = len(prices)

    max_p = 0

    for i in range(len_list):
        for j in range(i, len_list):
            max_p = max(prices[j]-prices[i], max_p)
    
    return max_p

print(bestStockTrade_bf(prices))

def bestStockTrade(prices):
    #profit = -sys.maxsize
    profit = 0 # in case of None 
    min_price = sys.maxsize

    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p-min_price)

    return profit

print(bestStockTrade(prices))
