class Real:
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
            found, ind = bsearch(self.__lst__, value);
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
    a = Real();
    a.insert(1.0);
    a.insert(2.0);
    a.insert(-1.0);
    a.insert(1.5);
    a.print();
    print(a.getMax());
    print(a.getMax());
    print(a.getMax());
    
        
