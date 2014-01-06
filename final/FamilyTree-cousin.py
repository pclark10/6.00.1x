from FamilyTree import *

def cousin(self, a, b):
    """
    Returns a tuple of (the cousin type, degree removed) 

    cousin type is an integer that is -1 if a and b
    are the same node or if one is the direct descendent 
    of the other.  Otherwise, cousin type is 0 or greater,
    representing the shorter distance to their common 
    ancestor as described in the exercises above.

    degree removed is the distance to the common ancestor

    Keyword arguments: 
    a -- string that is the name of a
    b -- string that is the name of b
    """
    nodeA = self.names_to_nodes[a]
    nodeB = self.names_to_nodes[b]
    ancestorsA = [nodeA]
    ancestorsB = [nodeB]
    
    while nodeA != self.root:
        nodeA = nodeA.get_parent()
        ancestorsA.append(nodeA)
        
    while nodeB not in ancestorsA:
        nodeB = nodeB.get_parent()
        ancestorsB.append(nodeB)
       
    ancestorsA = ancestorsA[:ancestorsA.index(nodeB) + 1]

    lenA = len(ancestorsA)
    lenB = len(ancestorsB)
    return (min(lenA, lenB) - 2, abs(lenA - lenB))

    #num = 0
    #numrem = 0
    #if a == b:
    #    return (-1, 0)
    #elif self.is_parent(a, b) or self.is_parent(b, a):
    #    return (-1, 1)
    #else:
    #    if self.names_to_nodes[a].parent == self.names_to_nodes[b].parent:
    #        num += 1
    #    
    #    return (num, numrem)