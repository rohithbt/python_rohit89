import os
newfile=open("ro.txt","r")  


#for i in range(1,10):
#    print(newfile.read())
newfile.seek(100)
print(newfile.tell())

