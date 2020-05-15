A=[]
A=[1,2,3,4]
print(A)
print(A[1])
print(A[3]) 


A[1] = "u can change the list element"
print(A[1])


B=[[1,2,3], 4 ,'third element',(1,2,3,4)] #A list can contain a list inside as well as a tuple
print(B)
print(B[3][3])

#lists are enclosed with  brackets[] and tuples with paranthesis()
#lists are mutable(cant change)
#tuples are immutable(can change)
#tuples are faster than lists