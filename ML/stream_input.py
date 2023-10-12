import pdb

# Returns the new average
# after including x
def getAvg(x, n, sum):
    sum = sum + x
    return float(sum) / n

# Prints average of a # stream of numbers
def streamAvg(arr):
	avg = 0;
	sum = 0;
	for i in range(1, len(arr)+1):
		avg = getAvg(arr[i-1], i , sum);
		sum = avg * i;
		print("Average of ", end = "");
		print(i, end = "");
		print(" numbers is ", end = "");
		print(avg);
	return;

# Driver Code
arr= [ 10, 20, 30, 40, 50, 60 ];
n = len(arr);
print(f"Input: {arr}/{n}")
streamAvg(arr);

