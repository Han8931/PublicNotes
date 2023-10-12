import time
import datetime

prices = [7, 1, 5, 3, 6, 4]
#prices = [1, 5, 5, 3, 6, 4]

def best_stock_trade(prices):
    total_val = 0

    prev = prices[1:]+[0]
    for i, j in zip(prices, prev):
        val = j-i
        if val>0:
            total_val+=val
    return total_val

def best_stock_trade2(prices):
    total_val = 0
    for i in range(len(prices)-1):
        if prices[i+1]-prices[i]>0:
            total_val+=prices[i+1]-prices[i]
    return total_val

def best_stock_trade3(prices):
    return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))

start = time.perf_counter()
print(best_stock_trade(prices))
elapsed_t = time.perf_counter()-start
print(datetime.timedelta(elapsed_t))

start = time.perf_counter()
print(best_stock_trade2(prices))
elapsed_t = time.perf_counter()-start
print(datetime.timedelta(elapsed_t))

start = time.perf_counter()
print(best_stock_trade3(prices))
elapsed_t = time.perf_counter()-start
print(datetime.timedelta(elapsed_t))


