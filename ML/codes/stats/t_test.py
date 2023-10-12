import scipy.stats as stats

# alpha/2 since it is two-sided
# N-1 degree of freedom, so 100-1
t_alpha = stats.t.ppf(1-0.025, 99) 
p = 1-stats.t.cdf(4.762, 99) 
print(t_alpha)
print(p)
