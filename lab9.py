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