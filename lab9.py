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
    def __init__(self, key, value, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value

class TempleArchive:
    """Binary Search Tree to store relics by ID."""
    def __init__(self):
        self.root = None
        self.n_relics = 0

    def add_relic(self,id,name,age):
        '''
        insert a relic into the BST
        '''
        if self.search_relic(id):
            raise AssertionError('Error: id is already stored')
        assert name is not None, 'Error: name must be a non-empty string'
        assert age > 0, 'Error: age must be a positive integer'
        relic_value = Relic(id,name,age)
        self.root = self._add_relic_help(self.root,id,relic_value)
        self.n_relics += 1
    
    def _add_relic_help(self,node,key,value):
        if node is None:
            return BSTNode(key,value)
        if node.key > key:
            node.left = self._add_relic_help(node.left,key,value)
        elif node.key < key:
            node.right = self._add_relic_help(node.right,key,value)
        return node

    def search_relic(self,id):
        return self._search_relic_help(self.root, id)
        
    def _search_relic_help(self, node, key):
        if node is None:
            return None
        if node.key > key:
            return self._search_relic_help(node.left, key)
        elif node.key < key:
            return self._search_relic_help(node.right, key)
        else:
            return node.value
    
    def remove_relic(self,id):
        if self.search_relic(id) is None:
            raise AssertionError(f'Error: relic with id {id} does not exist')
        self.root = self._remove_relic_help(self.root, id)
        self.n_relics -= 1
    
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
            node.key, node.value = succesor.key, succesor.value
            node.right = self._delete_min(node.right)
        return node

    def _find_min(self,node):
        while node.left is not None:
            node = node.left
        return node
    
    def _delete_min(self,node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        return node
    
    def list_relics(self):
        self._inorder_traversal(self.root)
    
    def _inorder_traversal(self,node):
        if node:
            self._inorder_traversal(node.left)
            print(node.value)
            self._inorder_traversal(node.right)        

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
    def __init__(self, max_size = 100):
        self.Heap = [None] * max_size
        self.size = max_size
        self.n = 0
    
    def add_task(self,task_name,priority):
        assert self.n < self.size
        assert isinstance(task_name,str) and task_name != '', 'Error: task must be a non-empty string'
        assert priority > 0, 'Error: priority must be a positive integer'
        current = self.n
        self.Heap[current] = ExcavationTask(task_name,priority)
        self.n += 1
        while (current > 0) and (self.Heap[current].priority < self.Heap[self._parent(current)].priority):
            parent = self._parent(current)
            self.Heap[current], self.Heap[parent] = self.Heap[parent], self.Heap[current]
            current = parent

    def _left_child(self,pos):
        assert pos<=(self.n//2)-1 #is internal node
        return (2*pos)+1
    
    def _right_child(self,pos):
        assert pos<=(self.n//2)-1 #is internal node
        return (2*pos)+2
        
    def _parent(self,pos):
        assert pos>0 #is not root
        return (pos-1)//2
        
    def get_next_task(self):
        assert self.n > 0, 'Error: queue is empty'
        return self.Heap[0]
    
    def complete_task(self):
        assert self.n > 0
        removed = self.Heap[0]
        self.Heap[0] = self.Heap[self.n-1]
        self.Heap[self.n-1] = None
        self.n -= 1
        if self.n > 0:
            self._sift_down(0)
        return removed
    
    def _sift_down(self,index):
        assert 0 <= index < self.n
        while not self.is_leaf(index):
            j = self._left_child(index)
            if j+1 < self.n and self.Heap[j+1].priority < self.Heap[j].priority:
                j += 1
            if self.Heap[index].priority <= self.Heap[j].priority:
                return
            self.Heap[index], self.Heap[j] = self.Heap[j], self.Heap[index]
            index = j            
        
    def is_leaf(self,index):
        return index>=self.n//2
        
    def list_tasks(self):
        queue_copy = ExcavationQueue(self.size)
        for i in range(self.n):
            queue_copy.Heap[i] = self.Heap[i]
        queue_copy.n = self.n
        while queue_copy.n>0:
            print(queue_copy.complete_task())