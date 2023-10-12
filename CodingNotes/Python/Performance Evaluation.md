```python
import datetime, time
start_t = time.perf_counter()
print(subset(nums))
elapsed_t = time.perf_counter() - start_t
print(f"{subset.__name__}: {datetime.timedelta(elapsed_t)}")
```