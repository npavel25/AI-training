class EmptyListException(Exception):
    pass

#it is bsearch() that was written for task 12
# no time to test its import, so just copy-paste
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

class RealContainer:
    def __init__(self):
        self.__lst__ = [];
        
    def insert(self, value):
        if 0 == len(self.__lst__):
            self.__lst__.append(value);
        else:
            found, ind = bsearch(self.__lst__, value);
            self.__lst__.insert(ind,value);
        
    def getByIndex(self, ind):
        if len(self.__lst__) != 0:
             return self.__lst__.pop(ind);
        else:
            raise EmptyListException("List is empty!");
            
    def getByValue(self, val):
        if len(self.__lst__) != 0:
            found, ind = bsearch(self.__lst__, val);
            if found:
                return self.__lst__.pop(ind);
            else:
                raise EmptyListException(str(val) + "is not in the list.");
        else:
            raise EmptyListException("List is empty!");
        
    def getMin(self):
        if len(self.__lst__) != 0:
             return self.__lst__.pop(0);
        else:
            raise EmptyListException("List is empty!");
            
    def getMax(self):
        if len(self.__lst__) != 0:
             return self.__lst__.pop(-1);
        else:
            raise EmptyListException("List is empty!");
            
    def print(self):
        print(self.__lst__);
            
if __name__ == "__main__":
    try:
        a = RealContainer();
        a.insert(1.0);
        a.insert(2.0);
        a.insert(-1.0);
        a.insert(1.5);
        a.print();
        print(a.getMax());
        print(a.getMax());
        print(a.getMax());
    except EmptyListException as ele:
        print(ele);
    try:
        b = RealContainer();
        b.getMax();
        b.getMin();
    except EmptyListException as ele:
        print(ele);
        
