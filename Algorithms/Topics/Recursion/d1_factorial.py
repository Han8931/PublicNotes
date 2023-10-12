# Basic 1
import time, datetime
from datetime import timedelta

number = 300

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

start_t_gen = time.perf_counter()
out = factorial(number)
eval_t = time.perf_counter()-start_t_gen
print(out)
print(f"Total Evaluation Time: {timedelta(seconds=eval_t)}", flush=True) 

def factorial2():
    a, b = 1, 2
    while True:
        yield a
        a, b = b*a, b+1

start_t_gen = time.perf_counter()
for i, a in enumerate(factorial2()):
    if i+2>number:
        print(a)
        break
eval_t = time.perf_counter()-start_t_gen
print(f"Total Evaluation Time: {timedelta(seconds=eval_t)}", flush=True) 
