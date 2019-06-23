class EmptyListException(Exception):
    pass

#optimized version
def bsearch(lst, value):
    print("list: ", lst);
    l = len(lst);
    mid = int(l/2);
    while mid < l:
        print("length: ", l, "middle: ", mid);
        if value < lst[mid]:
            l = mid;#res = bsearch(lst[:mid],value);
            mid = int(l / 2);
        elif value > lst[mid]:
            mid = mid + int( (l - mid ) / 2);
        else:
            res = mid;
            break;
    return res

##########################################################################################################
#recursive version. Not the best one
def bsearch_rcrsve(lst, value):
    #print("list: ", lst);
    l = len(lst);
    if 0 == l:
        raise EmptyListException(str(value) + " is not in the list.");
    mid = int(l / 2)
    #print("length: ", l, "middle: ", mid);
    if value < lst[mid]:
        res = bsearch(lst[:mid],value);
    elif value > lst[mid]:
        res = bsearch(lst[mid+1:],value);
        res += mid+1;
    else:
        res = mid;
    return res;

def Test_bsearch(lst,value):
    try:
        res = bsearch(lst,value);
        print("bsearch:", value, "found in position", res, "in the list", lst);
    except EmptyListException as ele:
        print(ele);    

if "__main__" == __name__:
    g
    # empty list
    lst = [];
    value = 3;
    Test_bsearch(lst, value);

    # 1 value
    lst = [3];
    value = 3;
    Test_bsearch(lst, value);

    # general case
    lst = [1,2,3,4,5,6];
    value = 3;
    Test_bsearch(lst, value);

    # Boundary case - minimum
    lst = [1,2,3,4,5,6];
    value = 1;
    Test_bsearch(lst, value);

    # Boundary case - maximum
    lst = [1,2,3,4,5,6];
    value = 6;
    Test_bsearch(lst, value);

    # value is not in the list
    lst = [2,4,6,8,10,12];
    value = 3;
    Test_bsearch(lst, value);
    value = 1;
    Test_bsearch(lst, value);
    value = 13;
    Test_bsearch(lst, value);

