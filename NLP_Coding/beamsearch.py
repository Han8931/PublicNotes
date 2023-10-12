import numpy as np
import pdb

# Define a sequence of 10 words over a vocab of 5 words
data = [[0.1, 0.2, 0.3, 0.4, 0.5],
		[0.5, 0.4, 0.3, 0.2, 0.1],
		[0.1, 0.2, 0.3, 0.4, 0.5],
		[0.5, 0.4, 0.3, 0.2, 0.1],
		[0.1, 0.2, 0.3, 0.4, 0.5],
		[0.5, 0.4, 0.3, 0.2, 0.1],
		[0.1, 0.2, 0.3, 0.4, 0.5],
		[0.5, 0.4, 0.3, 0.2, 0.1],
		[0.1, 0.2, 0.3, 0.4, 0.5],
		[0.5, 0.4, 0.3, 0.2, 0.1]]

data = np.array(data)

# Greedy Decoder

def greedyDecoder(data):
    return [np.argmax(x) for x in data]

result = greedyDecoder(data)
print(result)


def beamSearchDecoder(data, k):
    """
     - The local beam search algorithm keeps track of k states rather than just one. 
     - It begins with k randomly generated states. 
     - At each step, all the successors of all k states are generated. 
     - If any one is a goal, the algorithm halts. 
     - Otherwise, it selects the k best successors from the complete list and repeats.
    """

    sequences = [[[], 0.0]]

    # walk over each step in sequence
    for row in data:
        all_candidates = []
        # expand each current candidate
        for i in range(len(sequences)):
            seq, score = sequences[i]
            for j in range(len(row)):
                # -log, so lower socres are better
                # Keep tracking scores
                candidate = [seq + [j], score - np.log(row[j])] 
                all_candidates.append(candidate)
        # order all candidates by score
        ordered = sorted(all_candidates, key=lambda x:x[1])

        # select k best
        sequences = ordered[:k]
    return sequences

result = beamSearchDecoder(data, 3)

for seq in result:
    print(seq)
