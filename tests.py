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

archive.remove_relic(110) #remove relic
assert archive.search_relic(110) is None

#adding relic
archive.add_relic(75,"Relic 4",150)
archive.add_relic(125,"Relic 5",950)

#remove node with one child
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
queue = ExcavationQueue()
queue.add_task("stabilize ancient pillar",3)
queue.add_task("decode mystic tablet",1)
queue.add_task("secure hidden chamber",2)
queue.add_task("collect rare crystals",3)
queue.add_task("map subterranean tunnels",2)

assert queue.get_next_task().priority == 1

queue.complete_task()
assert queue.get_next_task().priority == 2

queue.complete_task()
assert queue.get_next_task().priority == 2

#empty queue
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
queue.list_tasks()
