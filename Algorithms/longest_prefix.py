import pdb

strs = ["x","y","z"]
strs = ["flower","flow"]

long_prefix = []
def longest_prefix(strs):
    for items in zip(*strs):
        test = set(items)
        if len(test)==1:
            long_prefix.append(items[0])
        else:
            break
    if long_prefix==None:
        return ""
    else:
        return "".join(long_prefix)

print(longest_prefix(strs))



