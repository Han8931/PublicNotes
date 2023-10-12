from functools import wraps

def eval_time_wrapper(func):
    @wraps(func)
    def function_wrapper(*args,**kwargs):
        start_t = time.perf_counter()
        output = func(*args,**kwargs)
        end_t = time.perf_counter()-start_t
        log = f"Elapsed Time: {timedelta(seconds=end_t)}"
        print(log, flush=True)
        return output

    return function_wrapper

