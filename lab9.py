# CSC 171 - Lab 9: The Temple of Forgotten Knowledge
# Abigail Briones Aranda
# Binary Search Tree (BST)

class Relic:
    """Represents a relic in the Temple Archive."""
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

class BSTNode:
    """Node of a Binary Search Tree."""
    def __init__(self, e = None, left = None, right = None):
        self.left = left
        self.right = right
        self.e = e
        self.ids = {}
        self.root = None
    
    def add_relic(self,id,name,age):
        #establish preconditions
        if id in self.ids:
            return
        if not name:
            return
        if age < 0:
            return
        #insert bst
    
    def add_relic_help(self,node):
        pass
    
    def search_relic(self,id):
        pass
    
    def remove_relic(self,id):
        pass
    
    def list_relics(self):
        pass


class TempleArchive:
    """Binary Search Tree to store relics by ID."""
    def __init__(self):
        self.n = 0

# Heap (Min-Heap)
class ExcavationTask:
    """Represents a task in the Excavation Queue."""
    # TODO: complete the definition

class ExcavationQueue:
    """Min-heap to manage excavation tasks by priority."""
    # TODO: complete the definition

# main code here