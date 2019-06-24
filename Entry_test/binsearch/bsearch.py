class EmptyListException(Exception):
    pass

#optimized version
def bsearch(lst, value):
    print("list: ", lst);
    found = False;
    l = len(lst);
    if 0 == l:
        raise EmptyListException("List is empty.");
    beg = 0; 
    end = l - 1;
    while beg <= end:
        mid = int( beg + (end - beg) / 2);
        if value < lst[mid]:
            end = mid - 1;
            res = beg;
        elif value > lst[mid]:
            beg = mid + 1;
            res = end + 1;
        else:
            found = True;
            res = mid;
            break;
    return found, res;

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
        found, res = bsearch(lst,value);
        if found:
            print("bsearch:", value, "found in position", res, "in the list", lst);
        else:
            print("bsearch:", value, "is not in the list", lst, "but it could be inserted in position: ", res);
    except EmptyListException as ele:
        print(ele);    

if "__main__" == __name__:

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

