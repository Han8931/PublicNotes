
cargo = [
        (4,12),
        (2,1),
        (10,4),
        (1,1),
        (2,2),
        ]

def fractional_knapsack_greedy(cargo):
    capacity = 15
    pack = []
    for p, w in cargo:
        pack.append((p/w, p, w))
    pack.sort(reverse=True)

    total_val = 0

    for val, p, w in pack:
        if capacity-w>=0:
            total_val+=p
            capacity-=w
        else:
            total_val+=p*capacity/w
            break
    return total_val

print(fractional_knapsack_greedy(cargo))
