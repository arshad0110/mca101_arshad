def sortMergeList( List1, List2,List3=[] ,in1=0, in2=0 ):
    
	    '''
	    objective : to merge two sorted list into one list
	    input : 
	            List1 : sorted list 1
	            List2 : sorted list 2
	            List3 : empty list 
            in1 : index of sorted list 1
	            in2 : index of sorted list 2
	    Output : 
	            List3 : merged list containing the different sorted list 
	    '''
	    '''
	    approach : using recursion
	    '''
	    
    assert in1 < (len(List1)+1)
    assert in2 < (len(List2)+1)
	
    if len(List1) == 0 and len(List2) == 0:
    print("Both List Are Empty")
	                
    elif len(List1) == 0:
        List3 = List2
	
    elif len(List2) == 0:
        List3 = List1
	
    elif ( List1[in1] < List2[in2] ) :
        List3.append(List1[in1])
        if( len(List1) > in1+1 ):
            List3 = sortMergeList(List1 ,List2,List3,in1+1 ,in2)
        else:
        
            List3 = List3 + List2[in2:]
	        
    elif ( List1[in1] > List2[in2] ) :
	List3.append(List2[in2])
	if( len(List2) > in2+1 ):
            List3 = sortMergeList(List1 ,List2,List3 ,in1 ,in2+1)
        else :
	    List3 = List3 + List1[in1:]
	    return List3
    elif(List1[in1]==List2[in2]):
	    List3.append(List1[in1])
	    List3 = List3 + List1[in2]
	
def main():
	        
    List1 = [int(x) for x in input("Enter the list 1 : ").split()]
    List2 = [int(x) for x in input("Enter the list 2 : ").split()]
    List3 = []
	
    print(sortMergeList(List1,List2,List3))
	
if __name__=='__main__':
    main()
