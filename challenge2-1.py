from itertools import combinations 

c = combinations([9, 5,3,2,1], 4) 


L = [9,9,9,9]

def solution(L):
    L.sort(reverse=True)
    sol = 0
    
    for i in range(len(L)):
        comb = list(combinations(L,len(L)-i))

        for j in comb:
            s = sum(j)
            if (s%3 == 0):
                
                for k in range(len(j)):
                    sol += j[k] * 10**(len(j)-1-k)
                return(sol)

    return(sol)


print(solution(L))