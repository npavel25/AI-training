class Real:
	def __init__(self):
	    self.__lst__ = [];
		
	def insert(self, value):
	    if 0 == len(__lst__):
		    __lst__.append(value);
		else:
	        ind = bsearch(__lst__, value);
		    __lst__.insert(ind,value);
		
	def getByIndex(self, ind):
	    if len(__lst__) != 0:
		     return __lst__.pop(ind);
	    else:
		    raise EmptyListException("List is empty!");
			
	def getByValue(self, val):
	    if len(__lst__) != 0:
		    ind = bsearch(__lst__, value);
		     return __lst__.pop(ind);
	    else:
		    raise EmptyListException("List is empty!");
		
    def getMin(self):
	    if len(__lst__) != 0:
		     return __lst__.pop(0);
	    else:
		    raise EmptyListException("List is empty!");
			
	def getMax(self):
	    if len(__lst__) != 0:
		     return __lst__.pop(-1);
	    else:
		    raise EmptyListException("List is empty!");
			
	def print(self):
	    print(__lst__);
			
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
	
		
