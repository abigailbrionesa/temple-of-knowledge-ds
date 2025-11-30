from lab9 import TempleArchive, ExcavationQueue

# TEMPLE ARCHIVE (BST)
archive = TempleArchive()
# searching non existant relic
assert archive.search_relic(1) is None
# adding relics
archive.add_relic(110,"Relic 1",500)
archive.add_relic(500,"Relic 2",1200)
archive.add_relic(650,"Relic 3",600)

assert archive.search_relic(500).name == "Relic 2"
assert archive.search_relic(110).age == 500
assert archive.search_relic(43) is None

archive.remove_relic(110) # remove leaf
assert archive.search_relic(110) is None

# adding relics
archive.add_relic(75,"Relic 4",100)
archive.add_relic(125,"Relic 5",900)

# remove node with one child
archive.remove_relic(125)
assert archive.search_relic(125) is None

try:
    empty_archive = TempleArchive()
    empty_archive.remove_relic(10)
    assert False
except AssertionError:
    pass

print("\nlist_relics:")
archive.list_relics()

# EXCAVATION QUEUE
q = ExcavationQueue()
q.add_task("Task a",3)
q.add_task("Task b",1)
q.add_task("Task c",2)
q.add_task("Task d",3)
q.add_task("Task e",2)

assert q.get_next_task().priority == 1 #peak

q.complete_task() #complete task
assert q.get_next_task().priority == 2

q.complete_task()
assert q.get_next_task().priority == 2

# empty queue
try:
    empty = ExcavationQueue()
    empty.get_next_task()
    assert False
except AssertionError:
    pass

try:
    empty = ExcavationQueue()
    empty.complete_task()
    assert False
except AssertionError:
    pass


print("\nlist_tasks:")
q.list_tasks()
