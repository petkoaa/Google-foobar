def solution(l):
# we search 'l' in pairs of x and y where x always comes before y and test if y%x==0
    # po means the position of .. in the input list 'l'
    po_y_devisible_by_x = {} # position z in this list represents the 'y' at pos z in 'l', and the value is the number of 'x' before 'z' by which "y" is divisible  
    po_x_which_devides_y = {} # position z in this list represents the 'x' at pos z in 'l', and the value is the number of 'y' after 'z' whiuch are devisible by "x"     
    count = 0

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if(l[j] % l[i] == 0): 
                po_y_devisible_by_x[j] = po_y_devisible_by_x.get(j, 0) + 1
                po_x_which_devides_y[i] = po_x_which_devides_y.get(i, 0) + 1
    for i in po_y_devisible_by_x:  # when the values in both dicts overlap thats when the number at pos 'i' in 'l' is the middle in a magic triplet 
        count += po_y_devisible_by_x[i] * po_x_which_devides_y.get(i, 0)

   
    return count
