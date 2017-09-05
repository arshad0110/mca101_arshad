#editing

list2=[]

def rec(list1):
    '''  
    Objective : to reverse the elements of the list
    input parameters:
        list1: list to be reversed
    return values : 
        list2 : reversed list
             
    '''
    #Approach : computing using length of the list
    
    length=len(list1)
    if list1==[]:
        return list2
    else:
        list2.append(list1[length-1])
        return rec(list1[0:length-1])
