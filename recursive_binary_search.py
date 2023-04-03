def recursive_binary_search(listt,target):
    if len(listt)==0:
        return False
    else:
        mid=len(listt)//2
        if listt[mid]==target:
            return True
        elif listt[mid]<target:
            return recursive_binary_search(listt[mid+1:], target)
        elif listt[mid]>target:
            return recursive_binary_search(listt[:mid:], target)
l=[1,2,3,4,5,6,7,8,9,10]

def verify(value):
    print("The target value is",value,sep=", ",end="    ")

check=recursive_binary_search(l, 12)

verify(check)

check=recursive_binary_search(l, 10)
verify(check)