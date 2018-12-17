def binarysearch(x,A,left,right):
    mid=left+round((right-left)/2)
    if(x==A[mid]):
        return mid
    elif(right==left):
        return
    elif(n < A[mid]):
        return(binarysearch(x, A, left, mid))
    else:
    return (binarysearch(x, A, mid+1, right))
