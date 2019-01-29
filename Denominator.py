def solution(A):
    # write your code in Python 3.6
    from collections import Counter
    if len(A)==0:
        return(-1)
    
        
    l=Counter(A).most_common(1)
        
        
    if l[0][1]>(len(A)/2):
        k=A.index(l[0][0])
        return(k)
    else:
        return(-1)
    pass