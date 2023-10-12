import itertools



def main()->None:
    # Count from 10
    for i in itertools.count(10):
        print(i)
        if i==15:
            break

    # Repeat
    for i in itertools.repeat(10, 4):
        print(i)

    # Accumulate
    for i in itertools.accumulate(range(1, 11)):
        print(i)

    # Permutations
    items = ["a", "b", "c"]
    perm = itertools.permutations(items) 
    for item in perm:
        print(item)

    # Permutations of two items
    items = ["a", "b", "c"]
    perm = itertools.permutations(items, 2) 
    for item in perm:
        print(item)

    # Combinations of two items
    items = ["a", "b", "c"]
    comb = itertools.combinations(items, 2) 
    for item in comb:
        print(item)

    # Combinations with replacement of two items
    items = ["a", "b", "c"]
    comb = itertools.combinations_with_replacement(items, 2) 
    for item in comb:
        print(item)

    # Change into a list
    comb = list(itertools.combinations_with_replacement(items, 2) )
    print(comb)

    # Chain
    items = ["a", "b", "c"]
    more_items = ["d", "e", "f"]
    chain = list(itertools.chain(items, more_items) )
    print(chain)

    # Filter false elements
    chain = list(itertools.filterfalse(lambda x: x%2==0, range(10)) )
    print(chain)

    # Take while traverses elements until get true
    chain = list(itertools.takewhile(lambda x: x%2==0, range(10)) )
    print(chain)

    # Star map
    star = list(itertools.starmap(lambda x, y: x*y, [(2, 6), (3, 4)]) )
    print(star)



if __name__ == "__main__":
    main()



