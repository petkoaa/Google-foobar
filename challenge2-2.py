from fractions import Fraction  


def solution(pegs):

    k = len(pegs)
    
    m = 0   #radius of first gear (2n)
    n = 0   #radius of last gear 


    t_p = 0     # the radius of the second to last gear a.k.a. the distance of last intersection minus the radius of the last gear (or n) 
    # find t_p 
    for i in range(0,k-2):
        if (i%2==0):
            t_p += pegs[k-2-i] - pegs[k-2-i-1]
        else:
            t_1 -= pegs[k-2-i] - pegs[k-2-i-1]


    # find n
    if(k%2==0):
    
        n =  float((pegs[k-1]-pegs[0]) - (pegs[k-2] - pegs[1]) - t_p - (pegs[1]-pegs[0])) /3 
        
        
    else:
        n = - ((pegs[k-1]-pegs[0]) - (pegs[k-2] - pegs[1]) - t_p - (pegs[1]-pegs[0]) )
    
      
    # m is must be 2*n    
    m = Fraction(2*n).limit_denominator()  #radius of first gear


    # check if the solution fullfills the requirements a.k.a that all gears are >=1 and fit on a single line 
    current_rad = m
    for i in range(0, k-1):
        distance_pegs = pegs[i+1] - pegs[i]
        next_rad = distance_pegs - current_rad
        if (current_rad < 1 or next_rad < 1):
            return [-1,-1]
        else:
            current_rad = next_rad

    return [m.numerator, m.denominator]


