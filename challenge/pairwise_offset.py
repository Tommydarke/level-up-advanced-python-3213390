def pairwise_offset(sequence, fillvalue="*", offset=0):
    sequence=list(sequence)
    sequence2=sequence.copy()
    
    x=0
    while offset > x:
        sequence.append(fillvalue)
        sequence2.insert(0, fillvalue)
        x=x+1

    sequence3=[]
    x = 0
    while x < len(sequence):
        myTuple=(sequence[x],sequence2[x])
        sequence3.append(myTuple)
        x=x+1
    #print(sequence3)
    return sequence3

#pairwise_offset('abcd', fillvalue='-', offset=1)


