import pdb 

s = 'II'
s = 'LVIII'
s = 'MCMXCIV'

num_dict = {'I':1 ,'V':5 ,'X':10 ,'L':50 ,'C':100 ,'D':500 ,'M':1000}

total = 0
i = 0

while i<len(s):
    if i+1<len(s) and num_dict[s[i]]<num_dict[s[i+1]]:
        temp = num_dict[s[i+1]]-num_dict[s[i]]
        total+=temp
        i+=2
    else:
        total+=num_dict[s[i]]
        i+=1

print(total)
    

        


