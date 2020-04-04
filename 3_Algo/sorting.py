def swap(deck, i, j):
    deck[i], deck[j] = deck[j], deck[i]


def insertion_sort(deck):
    for i in range(0,len(deck)):
        x=deck[i]
        j=i
        while j>0 and deck[j-1]>x:
            deck[j]=deck[j-1]
            j-=1
        deck[j]=x
    


def bubble_sort(deck):
    i=0
    for i in range(len(deck),1,-1):
        for j in range(0,i-1):
            if deck[j+1]<deck[j]:
                 swap(deck,j,j+1)


def selection(deck):
    i=0
    for i in range(0,len(deck)-1):
        minimum=i
        for j in range(i+1,len(deck)):
            if deck[j]<deck[minimum]:
                minimum=j
        if minimum!=i:
            swap(deck,i,minimum)
  
  
#merge
def merge_sort(A):
    """
    l'intelligence se trouve dans la fusion des tableaux
    """
    merge_sort_r(A, 0, len(A))
    
def merge_sort_r(A, start, end):
    if start < end -1:
        middle = (start+end)//2
        merge_sort_r(A, start, middle)
        merge_sort_r(A, middle, end)
        merge(A, start, middle, end)
        
def merge(A, start, middle, end):
    temp = [None]*len(A)
    i = start
    j = middle
    for k in range(start, end):
        if i < middle and j < end:
            if A[i] <= A[j]:
                temp[k] = A[i]
                i += 1
            else:
                temp[k] = A[j]
                j += 1
        else:
            if i < middle:
                temp[k] = A[i]
                i += 1
            else:
                temp[k] = A[j]
                j += 1
    A[start:end] = temp[start:end]
    
def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

def merge_sort_py(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    left = merge_sort_py(x[:mid])
    right = merge_sort_py(x[mid:])
    i = 0 # left index
    j = 0 # right index
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    # add the leftovers
    result += left[i:]
    result += right[j:]
    return result


#quick sort
def quick_sort(deck):
    """
    l'intelligence se trouve au niveau de la partition du tableau
    """
    quick_sort_r(deck, 0, len(deck)-1)

def quick_sort_r(deck, first, last):
    if first<last:
        pivot=partition(deck,first,last)
        quick_sort_r(deck,first,pivot-1)
        quick_sort_r(deck,pivot+1,last)
        
def partition(deck, first, last):
    pivot=deck[first]
    i=first
    j=last
    while i<=j:
        if deck[i]<=pivot:
            i+=1
        else:
            if deck[j]>pivot:
                j-=1
            else:
                swap(deck,i,j)
    swap(deck,first,j)
    return j
