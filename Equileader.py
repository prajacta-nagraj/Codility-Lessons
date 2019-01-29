def solution(A):
    # write your code in Python 3.6
    
    equi=0
    from collections import Counter
    #if len(A)==1:
        #return(0)
    for k in range(len(A)-1):
        if k==0:
            lower=[A[k]]
        else:
            lower=A[:k+1]
        
        
        upper=A[k+1:]
        
        l1=Counter(lower).most_common(1)
        l2=Counter(upper).most_common(1)
        
        if l1[0][1]>(len(lower)/2) and l2[0][1]>(len(upper)/2):
            if l1[0][0]==l2[0][0]:
                equi=equi+1
    return(equi)