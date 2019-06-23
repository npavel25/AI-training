class EmptyListException(Exception):
    pass

#recursive version. Not the best one
def bsearch(lst, value):
    print("list: ", lst);
    l = len(lst);
    if 0 == l:
        raise EmptyListException(str(value) + " is not in the list.");
    mid = int(l / 2)
    print("length: ", l, "middle: ", mid);
    if value < lst[mid]:
        res = bsearch(lst[:mid],value);
    elif value > lst[mid]:
        res = bsearch(lst[mid+1:],value);
        res += mid+1;
    else:
        res = mid;
    return res;
    
try:
    lst = [1,2,3,4,5,6];
    res = bsearch(lst,3);
    print("bsearch: ", res);
except Exception as e:
    print(e);
try:    
    lst = [2,4,6,8,10,12];
    res = bsearch(lst,3);
    print("bsearch: ", res);
except Exception as e:
    print(e);
        

