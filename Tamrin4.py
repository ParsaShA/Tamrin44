
lst1  = [1,2,3,4]
lst2 = [4,5,6,7]


def finder_odd(lst1,lst2):
    for i in lst1:
        if i not in lst2:
            print(i , end =' ')
    for j in lst2:
        if j not in lst1:
            print (j, end = ' ')
    
    
(finder_odd(lst1,lst2))