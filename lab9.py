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
        self.n_relics = 0
        self.root = None

    def add_relic(self,id,name,age):
        if self.search_relic(id) is not None:
            return
        if not name:
            return
        if age < 0:
            return
        self.root = self._add_relic_help(self,id,(name,age))
        self.n_relics += 1
        return
    
    def _add_relic_help(self,node,key,value):
        if node is None:
            return BSTNode(id,value)
        if node.key > key:
            self.left = self._add_relic_help(self,node,key,value)
        elif node.key < key:
            self.right = self._add_relic_help(self,node,key,value)
    
    def search_relic(self,id):
        return self._search_relic_help(self.root, id)
        
    def _search_relic_help(self, node, key):
        if node is None:
            return None
        if node.key < key:
            return self._search_relic_help(self, node.left, key)
        elif node.key > key:
            return self._search_relic_help(self, node.right, key)
        else:
            return node.value
    
    def remove_relic(self,id):
        self.root = self._remove_relic_help(self.root, id)
        self.size -= 1
        return
    
    def _remove_relic_help(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self._remove_relic_help(node.left,key)
        elif node.key < key:
            node.right = self._remove_relic_help(node.right,key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succesor = self._find_min(node.right)
            node.key, node.val = succesor.key, succesor.val
            node.right = self._delete_min(node.right)
            

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