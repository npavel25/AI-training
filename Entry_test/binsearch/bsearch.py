def bsearch(lst, value):
    print("list: ", lst);
    l = len(lst);
    mid = int(l / 2)
    print("length: ", l, "middle: ", mid);
    if value < lst[mid]:
        res = bsearch(lst[:mid],value);
    elif value > lst[mid]:
        res = bsearch(lst[mid+1:],value);
        res += len(lst[:mid+1]);
    else:
        res = mid;
    return res;
    
lst = [1,2,3,4,5,6];
res = bsearch(lst,3);
print("bsearch: ", res);
