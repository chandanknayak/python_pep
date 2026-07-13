"""Describe a method for performing a card shuffle of a list of 
2n elements,by converting it into two lists. A card shuffle 
is a permutation where a list L is cut into two lists, L1 and L2, 
where L1 is the first half of L and L2 is the second half of L, 
and then these two lists are merged into one by taking
the first element in L1, then the first element in L2, 
followed by the second element in L1, the second element in 
L2, and so on."""

def card_shuffle(L):
    n = len(L) 

    L1 = L[:n]
    L2 = L[n:]

    shuffled = []

    for i in range(n):
        shuffled.append(L1[i])
        shuffled.append(L2[i])

    return shuffled


L = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original List:", L)
print("Shuffled List:", card_shuffle(L))
