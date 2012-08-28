def quicksort(alist,first,last):
    if first<last:
        split=partition(alist,first,last)
        quicksort(alist,first,split-1)
        quicksort(alist,split+1,last)

def partition(alist,first,last):
    pivot=alist[first]
    leftmark,rightmark=first+1,last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<pivot:
            leftmark=leftmark+1
        while rightmark>=leftmark and alist[rightmark]>pivot:
            rightmark=rightmark+1
        if rightmark< leftmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
            
    alist[rightmark],alist[first]=alist[first],alist[rightmark]
    return rightmark

#----------------------------TEST---------------------------
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicksort(alist,0,8)
    
