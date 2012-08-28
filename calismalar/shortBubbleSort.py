def shortBubbleSort(alist):
     exchanges = True
     passnum = len(alist)-1
     while passnum > 0 and exchanges:
         exchanges = False
         for i in range(passnum):
             if alist[i]>alist[i+1]:
                 exchanges = True
                 alist[i],alist[i+1]=alist[i+1],alist[i]
         passnum = passnum-1
     return alist



#-----------------TEST---------------
alist=[234,56,345,6,87,4]
print shortBubbleSort(alist)
