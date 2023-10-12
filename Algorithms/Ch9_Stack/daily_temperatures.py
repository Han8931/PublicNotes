"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


A trick is to keep the indices of temperatures in a stack

"""
import pdb

temperatures = [73,74,75,71,69,72,76,73]


def dailyTemp(temperatures):
    wait_t = [0]*len(temperatures)
    stack = []

    for i, curr in enumerate(temperatures):
        while stack and curr>temperatures[stack[-1]]:
            last = stack.pop()
            wait_t[last] = i-last
        stack.append(i)
    return wait_t

print(dailyTemp(temperatures))


    


