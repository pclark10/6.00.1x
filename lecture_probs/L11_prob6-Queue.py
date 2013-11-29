class Queue(object):
    
    def __init__(self):
        self.vals = []
    
    def insert(self, e):
        self.vals.append(e)
    
    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError
            
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    
q = Queue()
q.insert(5)
q.insert(6)
q.insert(4)