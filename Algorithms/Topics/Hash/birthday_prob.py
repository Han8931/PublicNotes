import pdb
import random

n_trials = 10000
n_people = 23

def probSameBD(n_ppl, trials):
    """
    The birthday problem is to determine the probability 
    that in a randomly selected group of n people, at least two have the same birthday 
    (two will share a birthday).

    This problem tells us that collisions are quite common in hash problems.
    """
    same_bd = 0

    for _ in range(trials):
        birthdays = []
        for _ in range(n_ppl):
            p = random.randint(1, 365)
            if p not in birthdays:
                birthdays.append(p)
            else:
                same_bd+=1
                break

    print(f"BD Prob: {same_bd/n_trials*100:.2f}") 

probSameBD(n_people, n_trials)



