# CSC 171 - Lab 9: The Temple of Forgotten Knowledge
# Abigail Briones Aranda
# Binary Search Tree (BST)

class Relic:
    """Represents a relic in the Temple Archive."""
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.id}: {self.name} ({self.age} years old)'

class BSTNode:
    """Node of a Binary Search Tree."""
    def __init__(self, key, value, left = None, right = None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value

class TempleArchive:
    """Binary Search Tree to store relics by ID."""
    def __init__(self):
        self.n = 0
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
    
    def add_relic_help(self,node,e):
        pass
    
    def search_relic(self,id):
        pass
    
    def remove_relic(self,id):
        pass
    
    def list_relics(self):
        pass

# Heap (Min-Heap)
class ExcavationTask:
    """Represents a task in the Excavation Queue."""
    def __init__(self,task_name, priority):
        self.task_name = task_name
        self.priority = priority
        
    def __str__(self):
        return f'{self.priority}: {self.task_name}'

class ExcavationQueue:
    """Min-heap to manage excavation tasks by priority."""
    def __init__(self):
        self.count = 0
    
    def add_task(self,task_name,priority):
        pass
    
    def get_next_task():
        pass
    
    def complete_task():
        pass
    
    def list_tasks():
        pass

# main code here