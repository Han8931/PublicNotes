## String
#### Group Anagram
```python
import pdb
import collections

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(strs):
    anagrams = collections.defaultdict(list)
    for s in strs:
        # sorted returns a list of elements
        anagrams["".join(sorted(s))].append(s)  

    return anagrams

print(groupAnagram(strs))
```

#### Palindrome
```python
def longestPalindrome(s:str)->str:
    if len(s)<2 or s==s[::-1]:
        return s

    start = 0
    end = len(s)
    
    def searchPalindrome(left:str, right:str)->str:
        """
        Search the longest palindrome from strings with even or odd length 
        """
        while left>=start and right<end and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]

    longest = ''
    for i in range(len(s)-1):
        longest = max(searchPalindrome(i, i+1), searchPalindrome(i, i+2), longest, key=len)
    return longest

def palindrome(x):
    x = str(x)
    return True if x==x[::-1] else False
```

#### Most Common Words
```python
import re
import collections

import pdb

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWords(paragraph, banned):
    paragraph = paragraph.lower().split(" ")
    paragraph = [re.sub('[^a-z0-9]', '', word) for word in paragraph if word not in banned]
    return collections.Counter(paragraph).most_common(1)[0][0]

print(mostCommonWords(paragraph, banned))
```

## Array
#### Array Partition
```python
arr = [1,4,3,2]

def arrPart(arr):
    arr = sorted(arr)

    sums = 0
    for i in range(0, len(arr), 2):
        sums+=arr[i]

    return sums

def array_partition(array):
    return sum(sorted(array)[::2])

print(arrPart(arr))

```

#### Best to Time to Buy Stock
```python
import pdb
import sys

prices = [7,1,5,3,6,4]

def bestStockTrade(prices:list)->int:
    bf = 0
    min_p = sys.maxsize
    for p in prices:
        min_p = min(min_p, p)
        bf = max(p-min_p, bf)

    return bf

print(bestStockTrade(prices))

```

#### Product of Array except it self
```python
nums = [1,2,3,4]

def prodArr(nums:list)->list:
    if not nums:
        return 

    prod_ = 1
    left_p = []
    for i in range(len(nums)):
        left_p.append(prod_)
        prod_ *= nums[i]

    prod_ = 1
    for i in reversed(range(len(nums))):
        left_p[i]*=prod_
        prod_*=nums[i]

    return left_p

print(nums)
print(prodArr(nums))

```

#### Two Sum
```python
import pdb
from typing import List

def two_sum_faster(nums, target):
    """
    The index() method returns the index of the specified element in the list.
    """
    for i in range(0, len(nums)):
        complement = target-nums[i]
        if complement in nums[i+1:]:
            # Move i+1 thus, need to add i+1
            idx = nums[i+1:].index(complement)+(i+1)  
            return [i, idx]

def two_sum_dict(nums: List[int], target:int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num]=i
    
    for i, num in enumerate(nums):
        if target-num in nums_map:
            return [i, nums_map[target-num]]

nums = [3, 4, 6, 15]
target = 6
print(twoSum(nums, target))
```

#### Water Volume
```python
import pdb
from typing import List
import sys

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

def trapping_water(heights:List[int])->int:
    if not heights:
        return 

    vol = 0
    left = 0
    right = len(heights)-1
    left_max = 0
    right_max = 0

    while left<right:
        left_max = max(heights[left], left_max)
        right_max = max(heights[right], right_max)

        if left_max<=right_max:
            vol += left_max-heights[left]
            left+=1
        else:
            vol += right_max-heights[right]
            right-=1

    return vol

print(trapping_water(heights))

```

## Linked List
#### Linked List Implementation
```python
class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def print_ll(self,):
        if self.head:
            curr = self.head
            while curr:
                print(curr.val)
                curr = curr.next
        else:
            print("Empty list.")

```


#### Merge Two Sorted List
```python
def mergeTwoSortedList(l1, l2):

    head = Node(None) # tail
    curr = head

    left = l1
    right = l2

    while left and right:
        if left.val<right.val:
            curr.next = left
            left, curr  = left.next, left
        else:
            curr.next = right
            right, curr  = right.next, right
    
    while right:
        curr.next = right
        right, curr = right.next, right
    while left:
        curr.next = left
        left, curr = left.next, left

    return head.next
```


#### Odd Even 

```python
def oddEven(head):
    odd = node = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = even_head

    return head

```

#### Palindrome
```python
def isPalindromeLL3(head):
    if not head:
        return head

    q = collections.deque()

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q)>1:
        if q.popleft()!=q.pop():
            return False

    return True

def palindromeRunner(head):
    if not head:
        return 

    rev = None
    slow = head
    fast = head

    # This order is important
    # fast and fast.next
    while fast and fast.next:
    #while fast!=None and fast.next!=None:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val==slow.val:
        slow, rev = slow.next, rev.next

    return not rev # or, not slow


```

#### Reverse LL
```python
def reverse(head:Node)->Node:
    if not head:
        return 

    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

def reverseRec(head:Node)->Node:
    if not head:
        return 

    def reverse(node, prev=None):
        if node==None:
            return prev 
        nxt, node.next = node.next, prev 
        return reverse(nxt, prev=node)

    prev = reverse(head)

    return prev
```

#### Swap Nodes in Pairs
```python
def swapNodesPairs(head:Node)->Node:
    if not head or not head.next:
        return head

    temp = head.next
    head.next = revLLRec(temp.next)
    temp.next = head
    return temp

def swapPairs(head):
    if not head:
        return
    # Assign multiple names for this dummy node
    # Each name is independent
    root = prev = Node(None) 
    prev.next = head
    curr = head

    while curr and curr.next:
        temp = curr.next.next
        nxt = curr.next
        nxt.next = curr
        curr.next = temp
        prev.next = nxt
        prev = curr
        curr = temp

    return root.next

```

## Stack
#### Daily Temperature
```python
import pdb

temperatures = [73,74,75,71,69,72,76,73]

def dailyTemp(temperatures):
    wait = [0]*len(temperatures)
    stack = [] 

    for i, t in enumerate(temperatures):
        while stack and t>temperatures[stack[-1]]:
            last = stack.pop()
            wait[last] = i-last
        stack.append(i)

    return wait

print(dailyTemp(temperatures))
```

#### Valid Parentheses
```python
s = "([]{})"

def validP(s):

    stack = []
    table = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char not in table:
            stack.append(char)
        else: not stack or table[char]!=stack.pop():
            return False

    return len(stack)==0
```

#### Longest Substring
```python
s = "abcabcbb"

def longest_substring(s:str)->int:
    used = {}
    max_len = 0
    start = 0

    for i in range(len(s)):
        char = s[i]

        if char in used and start<=used[char]:
            start = used[char]+1
        else:
            max_len = max(max_len, i-start+1)

        used[char]=i

    return max_len

print(longest_substring(s))
```

## Hashing
#### Top-K Frequent Elements
```python
nums = [1,1,1,4,4,3]
def topkElements(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

print(topkElements(nums, 2))

```

## Graph
#### DFS
```python
def dfs(v):
    visited = []
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            for b in graph[n]:
                stack.append(b)

    return visited

def dfs_rec(v, visited=[]):
    visited.append(v)
    for n in graph[v]:
        if n not in visited:
            dfs_rec(n, visited)

    return visited

```

#### BFS
```python
def bfs(v):
    visited = [v]
    queue = [v]

    while queue:
        v = queue.pop(0)
        for n in graph[v]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

    return visited
```

## BackTracking
#### Number of Islands
```python
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


def numIsland(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]!='1':
            return 

        grid[i][j]="x"

        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i,j-1)

    count=0

    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                dfs(i,j)
                count+=1

    return count

print(numIsland(grid))
```

#### Permutations
```python
def permutations(nums:list)->int:

    perm = []
    prev_elements = []

    def dfs(elements):
        if len(elements)==0:
            perm.append(prev_elements[:])

        for n in elements:
            next_elements = elements[:]
            next_elements = next_elements.remove(n)
            prev_elements.append(n)

            dfs(next_elements)
            prev_elements.pop()
    
    dfs(nums)

    return perm
```

#### Combination
```python
def combinations(n:int, k:int)->list:

    comb = []
    prev_elem = []

    def dfs(elements, start, k):
        if k==0:
            comb.append(elements[:])
            return 

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], 1, k)
    return comb

```

#### Combination Sum
```python
def combination_sum(cand:list, tgt:int)->list:

    result = []
    prev_elem = []

    def dfs(elements):
        s = sum(prev_elem)
        if s==tgt:
            result.append(prev_elem[:])
        elif s>tgt:
            return 

        for i in range(len(elements)):
            next_elem = elements[:]

            prev_elem.append(elements[i])
            dfs(next_elem[i:])
            prev_elem.pop()

    dfs(cand)
    return result
```

## Binary Tree
#### Max Depth
```python
def maxDepth(root):
    if not root:
        return 0
    else:
        left = maxDepth(root.left)
        right = maxDepth(root.right)

    return max(left, right)+1
```

#### Diameter of Binary Tree

```python
class diameterBinTree():
    def __init__(self,):
        self.longest = 0 # This is very important

    def diameter(self, root):
        def dfs(node):
            if not node:
                return -1 # The height of Null node is treated as -1 

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2) # Diameter
            return max(left, right)+1  # Height

        dfs(root)
        return self.longest


```

##### Incorrect Solution
```python
# This is an incorrect solution due to the variable longest
def diameter(root):
    longest = 0 # This is an integer variabel

    def dfs(node):
        if not node:
            return -1 # The height of Null node is treated as -1 

        left = dfs(node.left)
        right = dfs(node.right)

        # This operation aggain longest variable again
        longest = max(longest, left+right+2) # Diameter
        return max(left, right)+1  # Height

    dfs(root)
    return longest

```

#### Invert Binary Tree
```python
def invertTree(root):
    if not root:
        return

    def dfs(node):
        if not node:
            return
        else:
            node.right, node.left = node.left, node.right

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return root

```

#### Is Balanced?
```python
class Solution:
	def isBalanced(self, root: Optional[TreeNode]) -> bool:
		if root is None:
			return True
	
	def height(node):
		if not node:
			return 0
		else:
			left = height(node.left)
			right = height(node.right)
		return max(left, right)+1
	
	left = height(root.left)
	right = height(root.right)
	if abs(left-right)>1:
		return False
	  
	lcheck = self.isBalanced(root.left)
	rcheck = self.isBalanced(root.right)
	if lcheck==True and rcheck==True:
		return True
```

#### Binary Tree Traverse

```python
def inorder(root):
    res = []

    def traverse(node):
        if not node:
            return
        
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)

    traverse(root)

    return res

def preorder(root):
    res = []

    def traverse(node):
        if not node:
            return
        
        res.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)

    return res

def postorder(root):
    res = []

    def traverse(node):
        if not node:
            return
        
        traverse(node.left)
        traverse(node.right)
        res.append(node.val)

    traverse(root)

    return res
```

## Other Problems
#### Unique Path
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
```

#### Climb Stairs
```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
         def climb(n):
             if n==1: #only one step option is availble
                 return 1
             if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
                 return 2
             return climb(n-1) + climb(n-2)
         return climb(n)
```

```python
```

```python
```

```python
```

```python
```

```python
```

