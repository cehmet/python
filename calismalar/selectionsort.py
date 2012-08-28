def selectionsort(alist):
    for index in range(len(alist),1,-1):
        max=0
        for i in range(1,index):
            if alist[i]>alist[max]:
                max=i
        index=index-1
        alist[index],alist[max]=alist[max],alist[index]
    return alist



#--------------TEST-----------------------
alist=[234,56,345,6,87,4]
print selectionsort(alist)
